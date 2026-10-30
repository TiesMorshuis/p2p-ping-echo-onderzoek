import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))

print ("Waiting for connection")
while True:
    data, address = sock.recvfrom(1024)
    print(f"Received from {address}: {data.decode()}")
    sock.sendto(data, address)

