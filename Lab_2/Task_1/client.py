import socket
import time


SERVER_IP = "SERVER_LAPTOP_IP"  # Fill in after both laptops join the hotspot.
PORT = 6015
SERVER_CLOSES_FIRST = False  # Set to True on both laptops for part (d).
MESSAGE = "Client ID: 23P0195; Server ID: 23P0111"


started = time.perf_counter()

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(5)
        client.connect((SERVER_IP, PORT))

        sent_at = time.perf_counter()
        client.sendall(MESSAGE.encode())
        reply = client.recv(4096)
        reply_ms = (time.perf_counter() - sent_at) * 1000

        if not reply:
            raise ConnectionError("Server closed without a reply")

        print("Reply:", reply.decode())
        print(f"Reply time: {reply_ms:.2f} ms")

        if SERVER_CLOSES_FIRST:
            while client.recv(4096):
                pass
        else:
            client.shutdown(socket.SHUT_WR)
            while client.recv(4096):
                pass

except OSError as error:
    elapsed_ms = (time.perf_counter() - started) * 1000
    print(f"Connection failed after {elapsed_ms:.2f} ms: {error}")
