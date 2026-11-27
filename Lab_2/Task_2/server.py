import socket


PORT = 6015

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", PORT))
    server.listen(1)
    print(f"Listening on TCP port {PORT}")

    run_number = 0
    while True:
        connection, address = server.accept()
        run_number += 1

        with connection:
            print(f"\nRun {run_number} from {address[0]}:{address[1]}")
            block_count = 0
            total_bytes = 0

            while True:
                block = connection.recv(4096)
                if not block:
                    break
                block_count += 1
                total_bytes += len(block)
                print(f"Block {block_count}: {len(block)} bytes")

            print(f"Total: {total_bytes} bytes in {block_count} blocks")