a=input("輸入一組四位數字為:")
x=a.split(" ")
b=(int(x[0])+7)%10
c=(int(x[1])+7)%10
d=(int(x[2])+7)%10
e=(int(x[3])+7)%10
print(d,e,b,c)