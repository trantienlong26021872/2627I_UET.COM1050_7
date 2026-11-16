a,b = map(float, input("nhap he so a va b trong phuong trinh ax+b=0: ").split())
if a!= 0:
    x=(-b)/a
    print("nghiem cua phuong trinh do la:",x)
elif a==0 and b== 0:
    print("phuong trinh co vo so nghiem ")
elif a==0 and b!= 0:
    print("phuong trinh vo nghiem")