import socket


PORT = 6015
B = 5
SERVER_CLOSES_FIRST = False  # Set to True on both laptops for part (d).


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", PORT))
    server.listen(1)
    print(f"Listening on TCP port {PORT}")

    while True:
        connection, address = server.accept()
        with connection:
            print(f"Client address: {address[0]}, port: {address[1]}")

            while True:
                message = connection.recv(4096)
                if not message:
                    break

                print("Received:", message.decode())
                reply = message.upper() if B % 2 else message[::-1]
                connection.sendall(reply)

                if SERVER_CLOSES_FIRST:
                    connection.shutdown(socket.SHUT_WR)
                    while connection.recv(4096):
                        pass
                    break