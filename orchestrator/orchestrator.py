# SOCKET
import argparse
import asyncio
import pathlib
import socket

# PARSING
import json
import time
import datetime

# Constants
MAX_CLIENT = 10
DATA_PATH = 'datasets/'
CACHE_PATH = 'cache.json'
LOGS_PATH = 'logs/orchestrator.log'
METADATA_PATH = 'metadata.json'
menu = b'[?] Choose (1=check|2=dispatch|3=exit):\n'

# Load mapping from cache
# def load_cache():

def write_logs(action, d_type, data):
    with open(LOGS_PATH, 'a') as file:
        file.write(f"\n{datetime.datetime.now()}: {action} for {d_type}: {data}")

def find_metadata_by_id(byte_text, cartid):
    json_string = byte_text.decode('utf-8')
    data = json.loads(json_string)["carts"]
    if str(cartid) not in data:
        return None
    return data[str(cartid)]
    
# METADATA
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
        writer.write(response)
        await writer.drain()
        write_logs("Successfully Queried", "cart metadata", cartid.decode())
        return 
    response = b"No Metadata\n"
    writer.write(response)
    await writer.drain()
    write_logs("Failed Fetch to metadata", "cart metadata", cartid.decode())
    return 

# DISPATCH
async def dispatch_cart(writer, path):
    full_path = DATA_PATH + path.decode()
    writer.write(f"Querying dataset: {full_path}\n".encode())
    await writer.drain()

    path = pathlib.Path(full_path)
    if path.is_file():
        writer.write(f"Dataset: {path.decode()} dispatched\n".encode())
        await writer.drain()
        # write to logs
        # update metadata
        return 
    else:
        raise Exception(f"Dataset doesn't exist: {path.decode()}".encode())

# HANDLER
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
                await dispatch_cart(writer, dataset)

            writer.write(b'[?] Would you like to make another request? (Y/N):\n')
            await writer.drain()
            answer = (await reader.readline()).strip()
            if answer == b'N':
                break
        elif option == b'3':
            break
        else:
            writer.write(b'Invalid option. Choose again\n')
            await writer.drain()

    writer.write(b'Closing connection...\n')
    await writer.drain()
    if writer.can_write_eof():
        writer.write_eof()

# SERVE
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


# CONFIGURE
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--host', type=str, default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=8080)
    args = parser.parse_args()
    print(f"Configuring server on host {args.host} port {args.port}")
    asyncio.run(serve(args.host, args.port))