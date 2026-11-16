a,b,c= map(float, input("nhap chieu dai ba canh cua tam giac: ").split())
def dien_tich():
    p= (a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
def chu_vi():
    C=a+b+c
    return C
if a>0 and b >0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("a,b,c la 3 canh cua tam giac deu.")
    elif a==b or a==c or b==c:
        print("a,b,c la 3 canh cua tam giac can")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("a,b,c la 3 canh cua tam giac vuong")
    else:
        print("a,b,c la 3 canh tam giac thuong")
    print(f"dien tich tam giac la: {dien_tich()}\nchu vi tam giac la:{chu_vi()}")
else:
    print("a,b,c khong la 3 canh tao thanh duoc mot tam giac")