import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

peer = ("192.168.2.9", 5000)

while True:
    message = b"PING"
    start = time.perf_counter()

    sock.sendto(message, peer)

    try:
        data, address = sock.recvfrom(1024)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"Received {data.decode()} in {elapsed:.2f} ms")
    except socket.timeout:
        print("Connection timed out")

    time.sleep(1)