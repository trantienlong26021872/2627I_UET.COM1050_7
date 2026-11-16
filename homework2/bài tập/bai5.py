a,b,c= map(float, input("nhap he so a,b,c trong phuong trinh ax**2 +b*x+c=0: ").split())
if a!=0:
    denta= b**2- 4*a*c
    if denta>0:
        x1=(-b+(denta)**(0.5))/(2*a)
        x2=(-b-(denta)**0.5)/(2*a)
        print(" hai nghiem cua phuong trinh:",x1,x2)
    elif denta==0:
        x=(-b)/(2*a)
        print(" phuong trinh co 1 nghiem la:",x)
    else:
        print("he phuong trinh vo nghiem")
elif a==0 and b!=0:
    x=(-c)/b
    print("phuong trinh tro thanh bac 1 va co nghiem duy nhat la",x)
elif a==0 and b==0 and c==0:
    print("phuong trinh co vo so nghiem")
else:
    print("phuong trinh vo nghiem")