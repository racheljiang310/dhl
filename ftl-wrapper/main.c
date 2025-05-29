#include "main.h"

int8_t cart_id = CART_ID;

int main(int argc, char * argv[]){
    uint8_t done = 1;

    if(argc < 2){
        println("client id required!");
        return 1;
    }

    client_request client;
    println("Welcome to the the cart server!");
    printf("I'm cart:%d\n", cart_id);
    while(done){
        char* buffer;
        scanf("Enter your request:%s\n", buffer);
        int result = parse_request(atoi(argv[1]), buffer, &client);
        if(result != 0){
            println("Someething went wrong when parsing.");
        }
        else{
            switch (client.type){
                case READ:
                    request_status response = read(client.client_id, &client);
                    break;
                case WRITE:
                    request_status response = write(client.client_id, &client);
                    break;
                default:
                    println("Unsupported request.");
                    break;
            }
        }
        char cont;
        scanf("Would you like to make another request? (Y/N): %c\n", &cont);
        if(cont == 'Y'){

        }
        else if(cont == 'N'){
            break;
        }else{
            println("Unsupported response.");
            break;
        }
    }
    println("Thank you for visiting my server! Goodbye!");
    return 0;
}

/// @brief buffer => request (TODO: work on this later)
/// @param client_id 
/// @param buffer 
/// @param request 
/// @return request format => nvme-[insert]|1|/dev/nvme0n1|1|32|5|simple_read.out
int parse_request(uint8_t client_id, char * buffer, client_request * request){
    
    return 0;
}

/// @brief discover the ssds that are connected to server
/// @param devices array of device names
/// @param ptr ptr to current top of devices array
/// @return request_status
request_status discover(uint8_t * ptr, char * devices){
 
    DIR *dp;
    struct dirent *entry;
    regex_t regex;
    ptr = devices;

    if (regcomp(&regex, "^nvme[0-9]+n[0-9]+$", REG_EXTENDED)) {
        fprintf(stderr, "Could not compile regex\n");
        return -1;
    }

    dp = opendir("/dev/");
    if (!dp) {
        perror("opendir");
        return EXIT_FAILURE;
    }

    while ((entry = readdir(dp)) != NULL) {
        if (regexec(&regex, entry->d_name, 0, NULL, 0) == 0) {
            devices[*ptr] = "/dev" + *(entry->d_name);
            ptr++;
        }
    }

    closedir(dp);
    regfree(&regex);
    return EXIT_SUCCESS;
}

/// @brief format: nvme read /dev/nvme0n1 --namespace-id=<nsid> --start-block=<slba> --block-count=<nblocks> --data=<output_file>
/// @param client_id 
/// @param request 
/// @return request_status
request_status read(uint8_t client_id, client_request * request){

    // format numbers as strings
    char slba[sizeof(uint16_t)];
    char nblocks[sizeof(uint16_t)];

    // format args
    char data_arg[64];
    char nsid_arg[64];
    char slba_arg[64];
    char nblocks_arg[64];

    // parse numbers to strings
    snprintf(slba, sizeof(slba), "%u", request->start_lba);
    snprintf(nblocks, sizeof(nblocks), "%u", request->num_blocks);

    // format
    snprintf(nsid_arg, sizeof(nsid_arg), "--namespace-id=%s", request->namespace_id);
    snprintf(slba_arg, sizeof(slba_arg), "--start-block=%s", slba);
    snprintf(nblocks_arg, sizeof(nblocks_arg), "--block-count=%s", nblocks);
    snprintf(data_arg, sizeof(data_arg), "--data=%s", request->output_file);

    // setup cmd args
    char *cmd[] = { "nvme", "read", 
                    (char *)request->devname,
                    nsid_arg, slba_arg, nblocks_arg, data_arg, 
                    (char *)NULL };

    // fork & exec
    pid_t pid = fork();

    if (pid == -1) {
        perror("fork failed");
        return REQUEST_INVALID;
    } else if (pid == 0) { // Child process: execute command
        execvp("nvme", cmd);
        perror("execvp failed"); // error handler
        exit(EXIT_FAILURE);
    } else { // Parent process: wait for child
        int status;
        waitpid(pid, &status, 0);
        if (WIFEXITED(status) && WEXITSTATUS(status) == 0) {
            return REQUEST_SUCCESS;
        } else {
            return REQUEST_INVALID;
        }
    }
}

/// @brief format: nvme write [to continue]
/// @param client_id 
/// @param request 
/// @return request_status
request_status write(uint8_t client_id, client_request * request){
    pid_t pid = fork();

    // format numbers as strings
    char slba[sizeof(uint16_t)];
    char nblocks[sizeof(uint16_t)];

    // format args ==> optiona?
    char data_arg[64];
    char nsid_arg[64];
    char slba_arg[64];
    char nblocks_arg[64];

    // parse numbers to strings
    snprintf(slba, sizeof(slba), "%u", request->start_lba);
    snprintf(nblocks, sizeof(nblocks), "%u", request->num_blocks);

    // format:  --start-block=0 --block-count=15 --data=data.raw
    snprintf(nsid_arg, sizeof(nsid_arg), "--namespace-id=%s", request->namespace_id);
    snprintf(slba_arg, sizeof(slba_arg), "--start-block=%s", slba);
    snprintf(nblocks_arg, sizeof(nblocks_arg), "--block-count=%s", nblocks);
    snprintf(data_arg, sizeof(data_arg), "--data=%s", request->output_file);

    // setup cmd args
    char *cmd[] = { "nvme", "write", 
                    (char *)request->devname,
                    nsid_arg, slba_arg, nblocks_arg, data_arg, 
                    (char *)NULL };

    if (pid == -1) {
        perror("fork failed");
        return REQUEST_INVALID;
    } else if (pid == 0) { // Child process: execute command
        execvp("nvme", cmd);
        perror("execvp failed"); // error handler
        exit(EXIT_FAILURE);
    } else { // Parent process: wait for child
        int status;
        waitpid(pid, &status, 0);
        if (WIFEXITED(status) && WEXITSTATUS(status) == 0) {
            return REQUEST_SUCCESS;
        } else {
            return REQUEST_INVALID;
        }
    }
    return REQUEST_SUCCESS;
}