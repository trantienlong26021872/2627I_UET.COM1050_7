a= int(input("nhap so giay de hoan thanh cong viec: "))
if a>=0:
    h=a//3600
    p=(a//60-h*60)
    s=a-h*3600-p*60
    print(f"{h} gio,{p} phut,{s} giay")
else:
    print("so lieu khong hop ly")