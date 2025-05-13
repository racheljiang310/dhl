# SOCKET
import argparse
import asyncio
import pathlib
import socket

# PARSING
import json
import time
import datetime

# CONSTS
DATA_PATH = 'datasets/'
METADATA_PATH = 'metadata.json'
LOGS_PATH = 'logs/orchestrator.log'
menu = b'[?] Choose (1:head|2:read|3:write|4:exit):\n'
# CACHE_PATH = 'cache.json'

######################################################################### LOGS
def write_logs(action, d_type, data):
    with open(LOGS_PATH, 'a') as file:
        file.write(f"\n{datetime.datetime.now()}: {action} for {d_type}: {data}")

######################################################################### PUSH DATASETS
# POST: This module is a read & write POST request from a random data server
# Typically used when the server wishes to modify data in a cart, or create/delete
async def write_data(writer, path):
    full_path = DATA_PATH + path.decode()
    file = pathlib.Path(full_path)
    print(f"Requested path: {full_path}\n")
    if file.is_file():
        writer.write(f"Dataset: {path.decode()} found\n".encode())
        await writer.drain()
        
        cart = None
        meta_path = pathlib.Path(METADATA_PATH)
        cart_data = json.loads(meta_path.read_bytes().decode())

        # finds first cart that isn't busy (status = 1)
        for key, value in cart_data["carts"].items():
            if path.decode() in value["datasets"] and value["status"] == 0: # status = 0 means available
                value["status"] = 1
                cart = value
                break

        if cart is not None:
            path_obj.write_text(json.dumps(cart_data, indent=4))
            print(f"Starting coroutine for dispatching cart {str(cart["id"])}")
            asyncio.create_task(dispatch(cart_data, str(cart["id"]), 5, path_obj))
            write_logs("Successfully Dispatch", "cart", cart["id"])
            return 
        else:
            writer.write(b"All carts are busy...\n")
            await writer.drain()
            write_logs("Failed Dispatch to dataset", "dataset name", path.decode())
    else:
        writer.write(b"Dataset doesn't exist\n")
        await writer.drain()
        write_logs("Failed Dispatch to dataset", "dataset name", path.decode())
        return

######################################################################### METADATA
def find_metadata_by_id(byte_text, cartid):
    json_string = byte_text.decode('utf-8')
    data = json.loads(json_string)["carts"]
    if str(cartid) not in data:
        return None
    return data[str(cartid)]

# HEAD: This module fetches metadata about a specific cart based on cart-id
async def fetch_metadata(writer, cartid):
    path = pathlib.Path(METADATA_PATH)
    if path.is_file():
        response = b"Metadata: "
        metadata = find_metadata_by_id(path.read_bytes(), cartid.decode())
        if metadata == None:
            response = b'Cart not found...\n'
            writer.write(response)
            await writer.drain()
            write_logs("Failed Queried", "cart metadata", cartid.decode())
            return 
        response += b'id: '+str(metadata["id"]).encode() + b' | '
        response += b'status: '+str(metadata["status"]).encode() + b' | '
        response += b'size: '+str(metadata["size"]).encode() + b' | '
        response += b'space: '+str(metadata["space"]).encode() + b'\n'
        for dset in metadata["datasets"]:
            response += b'dataset: '+str(dset).encode() + b'\n'
        writer.write(response)
        await writer.drain()
        write_logs("Successfully Queried", "cart metadata", cartid.decode())
        return 
    response = b"No Metadata\n"
    writer.write(response)
    await writer.drain()
    write_logs("Failed Fetch to metadata", "cart metadata", cartid.decode())
    return 

######################################################################### DISPATCH
async def dispatch(metadata, key, delay, path):
    await asyncio.sleep(delay)
    metadata["carts"][key]["status"] = 0
    path.write_text(json.dumps(metadata, indent=4))
    print(f"Finished coroutine for dispatching cart {str(metadata["carts"][key]["id"])}")
    write_logs("Successful return after dispatch", "cart", str(key))

# POST: This module is a read-only POST request from a random data server
# Typically used when the server wishes to train a model and needs the data form a cart
async def read_from_cart(writer, path):
    full_path = DATA_PATH + path.decode()
    writer.write(f"Fetching dataset: {full_path}\n".encode())
    await writer.drain()

    file = pathlib.Path(full_path)
    if file.is_file():
        writer.write(f"Dataset: {file} will be dispatched\n".encode())
        await writer.drain()
        
        cart = None
        path_obj = pathlib.Path(METADATA_PATH)
        cart_data = json.loads(path_obj.read_bytes().decode())

        # finds first cart that isn't busy (status = 1)
        for key, value in cart_data["carts"].items():
            if path.decode() in value["datasets"] and value["status"] == 0: # status = 0 means available
                value["status"] = 1
                cart = value
                break

        if cart is not None:
            path_obj.write_text(json.dumps(cart_data, indent=4))
            print(f"Starting coroutine for dispatching cart {str(cart["id"])}")
            asyncio.create_task(dispatch(cart_data, str(cart["id"]), 5, path_obj))
            write_logs("Successfully Dispatch", "cart", cart["id"])
            return 
        else:
            writer.write(b"All carts are busy...\n")
            await writer.drain()
            write_logs("Failed Dispatch to dataset", "dataset name", path.decode())
    else:
        writer.write(b"Dataset doesn't exist\n")
        await writer.drain()
        write_logs("Failed Dispatch to dataset", "dataset name", path.decode())
        return

async def write_to_cart(writer, cartid, dname):
    cart = None
    path_obj = pathlib.Path(METADATA_PATH)
    metadata = json.loads(path_obj.read_bytes().decode())

    for key, value in metadata["carts"].items(): # find cart obj
        if str(cartid) == key:
            value["status"] = 1
            cart = value
            break

    if cart is not None:
        path_obj.write_text(json.dumps(metadata, indent=4))
        print(f"Starting coroutine for dispatching cart {str(cart["id"])}")
        asyncio.create_task(dispatch(metadata, str(cart["id"]), 10, path_obj))
        write_logs("Successful Dispatch", "cart", cart["id"])
        return 
    else:
        writer.write(b"Unexpected failure...\n")
        await writer.drain()
        write_logs("Failed Dispatch to dataset", "dataset name", path.decode())

# STATIC: This function will fetch all the available carts to add data to
# returns byte-encoded list of available carts, else return error message
def list_available_carts(gigs):
    available = []
    response = None
    path = pathlib.Path(METADATA_PATH)
    if path.is_file():
        metadata = json.loads(path.read_bytes().decode())
        if metadata == None:
            print('Metadata not found...\n')
            return 
        for key, value in cart_data["carts"].items():
            if value["status"] == 0 and (value["space"]) >= gigs:
                available.append(value["id"])
        response = "Available: "
        response += '|'.join(str(x) for x in available)
    if response == None:
        return (0, b"No available carts at the moment")
    return (1, response.encode())

######################################################################### CLIENT INTERFACE
async def handler(reader, writer):
    global menu
    writer.write(b'Welcome to the Cart Whispherer Server!\n')
    await writer.drain()

    while True:
        writer.write(menu)
        await writer.drain()

        option = (await reader.readline()).strip()
        # print(f"Got option: {option}")

        if option == b'1' or option == b'2':
            if option == b'1':
                writer.write(b'[?] Enter a cart id:\n')
                await writer.drain()
                cart = (await reader.readline()).strip()
                await fetch_metadata(writer, cart)
            elif option == b'2':
                writer.write(b'[?] Enter a dataset:\n')
                await writer.drain()
                dataset = (await reader.readline()).strip()
                await read_from_cart(writer, dataset)
            elif option == b'3':
                # fetch data set name
                writer.write(b'[?] Dataset name:\n')
                await writer.drain()
                dataset = (await reader.readline()).strip()

                # fetch the size
                writer.write(b'[?] Dataset size (GB):\n')
                await writer.drain()
                datasize = (await reader.readline()).strip()
                
                # shows client available carts to write to
                listing = list_available_carts((int)(datasize))
                writer.write(listing[1])
                await writer.drain()
                if listing[0] == 1: # there are available carts
                    # prompts client to choose a cart to dispatch
                    writer.write(b'[?] Choose a cart (id):\n')
                    await writer.drain()
                    cartid = (await reader.readline()).strip()
                    await write_to_cart(writer, cartid)

            writer.write(b'[?] Would you like to make another request? (Y/N):\n')
            await writer.drain()
            answer = (await reader.readline()).strip()
            if answer == b'N':
                break
        elif option == b'4':
            break
        else:
            writer.write(b'Invalid option. Choose again\n')
            await writer.drain()

    writer.write(b'Closing connection...\n')
    await writer.drain()
    if writer.can_write_eof():
        writer.write_eof()

async def serve(host, port):

    async def handle(reader, writer):
        try:
            await handler(reader, writer)
        except Exception as e:
            print(e)

        writer.close()
        await writer.wait_closed()

    print(f"Startup routine...")
    server = await asyncio.start_server(handle, host=host, port=port)

    async with server:
        await server.serve_forever()


######################################################################### SERVER CONFIG
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--host', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=8080)
    args = parser.parse_args()
    print(f"Configuring server on host {args.host} port {args.port}")
    asyncio.run(serve(args.host, args.port))