a,b=map(float, input("nhap chieu dai canh a va b").split())
if a>0 and b>0:
    S=a*b
    C= (a+b)*2
    print("Dien tich hinh chu nhat:",S)
    print("Chu vi hinh chu nhat:",C)
else:
    print("a va b khong tao ra hinh chu nhat.")