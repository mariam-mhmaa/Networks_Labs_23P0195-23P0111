import socket
import time


SERVER_IP = "SERVER_LAPTOP_IP"  # Fill in after both laptops join the hotspot.
PORT = 6015
B = 5
H = 1 + (B % 3)  # 3 seconds
USE_TIMEOUT = True  # Set to False for part (d).


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP, PORT))
    client.settimeout(3 * H if USE_TIMEOUT else None)
    last_ping = time.monotonic()

    try:
        with client.makefile("r") as incoming:
            while True:
                line = incoming.readline()
                if not line:
                    elapsed = time.monotonic() - last_ping
                    print(f"{time.strftime('%H:%M:%S')} server closed connection")
                    print(f"{elapsed:.1f} seconds after last PING")
                    break

                ping = line.strip()
                print(f"{time.strftime('%H:%M:%S')} {ping}")
                last_ping = time.monotonic()

                number = ping.split()[1]
                pong = f"PONG {number}"
                client.sendall((pong + "\n").encode())
                print(f"{time.strftime('%H:%M:%S')} {pong}")

    except socket.timeout:
        elapsed = time.monotonic() - last_ping
        print(f"{time.strftime('%H:%M:%S')} link lost")
        print(f"{elapsed:.1f} seconds after last PING")
