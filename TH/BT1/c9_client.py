#client
import socket
#socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sendto
msg="hi there\n"
s.sendto(msg.encode('ascii'), ('127.0.0.1', 9999))
#recvfrom
data, (a,p) = s.recvfrom(10224)
print(data.decode('ascii'))
#close
s.close()