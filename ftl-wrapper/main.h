#ifndef MAIN_H
#define MAIN_H

#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <stdlib.h>
#include <dirent.h>
#include <pthread.h>
#include <sys/wait.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/syscall.h>

#define CART_ID 1

typedef enum {
    READ,
    WRITE,
} request_type;

/// @brief a "read" request to the "cart server"
typedef struct {
    char * dname;
    char * devname;
    char * namespace_id;
    char * output_file;
    request_type type;

    uint8_t client_id;
    uint8_t cart_id;


    uint16_t size;
    uint16_t num_blocks;
    uint16_t start_lba;
} client_request;

/// @brief any "request" sends a status response
typedef enum {
    REQUEST_SUCCESS,
    REQUEST_INVALID,
    REQUEST_TIMEOUT,
    REQUEST_UNAUTH,
} request_status;

int parse_request(uint8_t client_id, char * buffer, client_request * request);
request_status read(uint8_t client_id, client_request * request);
request_status write(uint8_t client_id, client_request * request);
#endif