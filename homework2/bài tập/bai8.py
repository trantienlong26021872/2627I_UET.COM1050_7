a,b,m,c,d,n=map(float, input("nhap lan luot he so a,b,m,c,d,n cua he phuong trinh ").split())
A=a*d-b*c
B=m*d-b*n
if A!=0:
    x=B/A
    if b!=0:
        y=(m-a*x)/b
    else:
        y=(n-c*x)/d
    print("he phuong trinh co nghiem la",x,y)
else:
    if a==0 and b==0 and c==0 and d==0:
        if m==0 and n==0:
            print("he phuong trinh co vo so nghiem")
        else:
            print("he phuong trinh vo nghiem")
    else:
        if B==0:
            print("he phuong trinh co vo so nghiem")
        else:
            print("he phuong trinh vo nghiem")
