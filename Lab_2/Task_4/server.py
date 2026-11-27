import socket


PORT = 7015

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind(("", PORT))
    print(f"Listening on UDP port {PORT}")

    try:
        while True:
            data, address = server.recvfrom(65535)
            print(
                f"{address[0]}:{address[1]} | "
                f"length={len(data)} | first 20={data[:20]!r}"
            )
    except KeyboardInterrupt:
        print("\nServer stopped")