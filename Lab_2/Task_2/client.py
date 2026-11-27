import socket


SERVER_IP = "192.168.1.200"  
PORT = 6015
A = 1
B = 5
M = 5 + A


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP, PORT))
    total_bytes = 0

    for k in range(1, M + 1):
        letter = chr(ord("A") + k - 1)
        message = f"{k}:" + letter * (10 * (k + B))
        client.sendall(message.encode("ascii"))
        total_bytes += len(message)
        print(f"Sent message {k}: {len(message)} bytes")

    client.sendall(b"Z" * 5000)
    total_bytes += 5000
    print("Sent final message: 5000 bytes")
    print(f"Total sent: {total_bytes} bytes")
