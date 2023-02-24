"""
6) Viết hàm trả về: 
- số lớn nhất trong danh sách (list) các số
- tổng các số trong danh sách.
- tích các số trong danh sách.
"""
lst = []
#ham nhap danh sach
def enter_list(n):
    for i in range(n):
        print("\tPhan tu thu", i+1, "la:", end=" ")
        lst.append(int(input()))
    return lst
#ham tim so lon nhat
def find_max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
#ham tinh tong ds
def sum_list(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
#ham tinh tich ds
def tich_list(arr):
    tich = 0
    for i in arr:
        tich = n*i
    return tich


# Chuong trinh chinh
n = int(input("Nhap vao so luong phan tu: n = "))
print("Nhap vao mang:")
arr = enter_list(n)


print("\nPhan tu lon nhat la: ", find_max(arr))
print("\nTong cac so trong danh sach: ", sum_list(arr))
print("\nTich cac so trong danh sach: ", tich_list(arr))