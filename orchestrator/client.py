import argparse
import asyncio

async def communicate(reader, writer):
    try:
        while True:
            line = await reader.readline()
            if not line:
                print("Connection closed by server.")
                break

            line_decoded = line.decode().strip()
            print(line_decoded)

            if line.startswith(b'[?]'):
                response = input("> ")
                writer.write((response + '\n').encode())
                await writer.drain()
    except asyncio.CancelledError:
        print("\nCommunication cancelled.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def client():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--server-host', type=str,   default='127.0.0.1')
    parser.add_argument('-p', '--server-port', type=int,   default=8080)
    args = parser.parse_args()

    try:
        reader, writer = await asyncio.open_connection(args.server_host, args.server_port)
        await communicate(reader, writer)
    except ConnectionRefusedError:
        print(f"Could not connect to {args.server_host}:{args.server_port}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(client())
    except KeyboardInterrupt:
        print("\nClient disconnected.")