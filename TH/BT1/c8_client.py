#client
import socket
#socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sendto
s.connect(('127.0.0.1', 9999))
#recvfrom
msg=s.recv(1024)
print(msg.decode('ascii'))
#close
s.close()
