a={"1":72,"2":62,"3":82,"4":44,"5":60}
r={"A":55,"B":68}
b=str(input("請選擇主餐:"))
n=str(input("升級的套餐:"))
c=str(input("是否升級成大杯飲料:"))
d=str(input("是否換成大薯:"))
if(c=="是" and d=="是"):
    print(a.get(b)+r.get(n)+7+13)
elif(c=="是" and d!="是"):
    print(a.get(b)+r.get(n)+7)
elif(c!="是" and d=="是"):
    print(a.get(b)+r.get(n)+13)    
else:
    print(a.get(b)+r.get(n))