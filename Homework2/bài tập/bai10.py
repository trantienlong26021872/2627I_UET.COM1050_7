a,b=map(float, input("nhap toa do tam duong tron: ").split())
x,y=map(float, input("nhap toa do muon xet: ").split())
r=float(input("nhap chieu dai ban kinh duong tron: "))
if (x-a)**2+(y-b)**2==r**2:
    print("diem nam tren duong tron")
elif (x-a)**2+(y-b)**2>r**2:
    print("diem nam ngoai duong tron")
else:
    print("diem nam trong duong tron") 
  