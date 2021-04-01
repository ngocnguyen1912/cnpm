import sys
tong=0
while True:
    s=input(" nhap nhat ky giao dich")
    if not s:
        break
    value=s.split(" ")
    hinhthuc=value[0]
    tien=int(value[1])
    if(hinhthuc=="D"):
        tong+=tien
    elif(hinhthuc=="W"):
        tong-=tien
    else:
        pass
print(tong)
import sys
sum=0
while True:
    s=input("moi nhap: ")
    if not s:
        break
    value=s.split(" ")
    hinhthuc=value[0]
    tien=int(value[1])
    if(hinhthuc=="D"):
        sum+=tien
    elif(hinhthuc=="W"):
        sum-=tien
    else:
        pass
print(sum)
