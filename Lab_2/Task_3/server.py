import socket
import time


PORT = 6015
H = 3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", PORT))
    server.listen(1)
    print(f"Listening on TCP port {PORT}")

    try:
        while True:
            connection, address = server.accept()
            with connection, connection.makefile("r") as incoming:
                print(f"Client: {address[0]}:{address[1]}")
                number = 1
                next_ping = time.monotonic()

                while True:
                    wait = next_ping - time.monotonic()
                    if wait > 0:
                        time.sleep(wait)

                    ping = f"PING {number}"
                    connection.sendall((ping + "\n").encode())
                    print(f"{time.strftime('%H:%M:%S')} {ping}")

                    pong = incoming.readline()
                    if not pong:
                        print("Client closed connection")
                        break
                    print(f"{time.strftime('%H:%M:%S')} {pong.strip()}")

                    number += 1
                    next_ping += H

    except KeyboardInterrupt:
        print("\nServer stopped")