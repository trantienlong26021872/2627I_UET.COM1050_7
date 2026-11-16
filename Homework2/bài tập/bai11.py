x,y= map(float, input("nhap lan luot x y: ").split())
if x==0 and y <0 :
    print(" 0 mu voi so am la phep tinh khong tinh duoc")
elif x==0 and y==0:
    print("0 mu 0 la phep tinh khong tinh duoc")
elif x<0 and y!=int(y):
    print("mot so am co so mu la mot so thap phan thi tinh la so phuc")
else:
    c= x**y
    print("dap an la:",c)