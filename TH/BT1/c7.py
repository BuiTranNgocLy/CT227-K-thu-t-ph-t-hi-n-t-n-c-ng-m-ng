"""
7) Viết chương trình cho biết:
- tên của máy tính cục bộ
- địa chỉ IP của www.ctu.edu.vn
- tên máy tính có địa chỉ: 123.30.143.225
"""
import socket
#Ten may tinh cuc bo
host_name = socket.gethostname()
print("Host name: %s" %host_name)

#dia chi IP cua www.ctu.edu.vn
addr = socket.gethostbyname('www.ctu.edu.vn')
print("IP address: %s " %addr)

#Ten may tinh co dia chi 123.30.143.225
ip = socket.gethostbyaddr('123.30.143.225')
print("Host name: ", ip)           