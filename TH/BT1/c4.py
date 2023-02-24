"""
S = 1 + 2 + ... + n 
S1 = 1 + 3 + ... + (2n - 1) 
S2 = 2 + 4 + ... + 2n
n nhap tu ban phim
"""
n = int(input("Nhap n: "))
s=0
#Tinh S = 1 + 2 + ... + n
for i in range(0, n+1):
    s += i
print("KQ phep tinh S= ",s)

#Tinh S1 = 1 + 3 + ... + (2n - 1)
s1=0
for i in range(1, n+1):
    s1 += (2*i-1)
print("KQ phep tinh S1= ",s1)

#Tinh S2 = 2 + 4 + ... + 2n
s2=0
for i in range(1, n+1):
    s2 += 2*i
print("KQ phep tinh S2= ",s2)