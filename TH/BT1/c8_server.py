"""
8) Viết chương trình hello server và client giao tiếp thông qua cổng 9999,
sử dụng giao thức TCP. Hello server chỉ phục vụ cho 1 client nối kết tại 1 thời điểm.
Khi client nối kết đến, hello server gửi lời chào đến client và nhận lời chào từ client gửi đến nó.
"""
#server
import socket
#socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind
#s.bind((host_name, port))
s.bind(('', 9999))
#listen
s.listen(5)
while True:
    #accpet
    cli, (remhost, remport) = s.accept()
    #recv
    print("Da nhanket noi tu: ", remhost)
    #thong diep
    msg= "Hello %s\n" %remhost
    #send
    cli.send(msg.encode('ascii'))
    #close
    cli.close()