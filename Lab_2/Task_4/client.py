import socket


SERVER_IP = "SERVER_LAPTOP_IP"  # Fill in after both laptops join the hotspot.
PORT = 7015
A = 1
B = 5
M = 5 + A
PART = "a"  # Use "a" for (a) and (b), then "c", "d", or "e".


def send(client, data, label):
    try:
        sent = client.sendto(data, (SERVER_IP, PORT))
        print(f"{label}: sent {sent} bytes")
    except OSError as error:
        print(f"{label}: send failed: {error}")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    if PART == "a":
        for k in range(1, M + 1):
            letter = chr(ord("A") + k - 1)
            message = (f"{k}:" + letter * (10 * (k + B))).encode("ascii")
            send(client, message, f"Message {k}")
        send(client, b"Z" * 5000, "Final message")

    elif PART == "c":
        for size in (1472, 1473, 1000 * (A + 2)):
            send(client, b"X" * size, f"{size}-byte datagram")

    elif PART == "d":
        for size in (65507, 65508):
            send(client, b"X" * size, f"{size}-byte datagram")

    elif PART == "e":
        send(client, b"Server stopped", "One datagram")

    else:
        print("Choose PART = 'a', 'c', 'd', or 'e'")
