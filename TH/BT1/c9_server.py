"""
Viết chương trình hello server và client giao tiếp thông qua cổng 9999, sử dụng giao thức UDP.
Hello server chỉ phục vụ cho 1 client nối kết tại 1 thời điểm.
Khi client nối kết đến, hello server gửi lời chào đến client và nhận lời chào từ client gửi đến nó
"""
#server_UDP
import socket
#socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind
s.bind(('', 9999))
while True:
    #recvfrom
    data, (a,p) = s.recvfrom(1024)
    print("Nhan ket noi tu: ", a)
    msg= "Hello %s\n" %a
    #sendto
    s.sendto(msg.encode('ascii'), (a,p))
