import socket
hostname = socket.gethostname()
adres = socket.gethostbyname(hostname)
print("IP Adresi : "+ adres)