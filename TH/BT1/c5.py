"""
5) Viết chương trình đổi số nguyên hệ mười ra số nhị phân
"""
# Xay dung ham
def Dec2Bin(n):
    k = []
    while (n>0):
        a = int(float(n%2)) # Tinh phan du
        k.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo

    kq = ""
    k.reverse() # Dao nguoc danh sach
    # Chuyen doi list sang string
    for i in k:
        kq += str(i)

    return kq
# Chuong trinh chinh
n = int(input("Nhap vao so thap phan: "))
print("So", n," co dang nhi phan la:", Dec2Bin(n))