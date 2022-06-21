a=int(input("請輸入正整數n:"))
b=0

for i in range(1,a+1):
    if a%i==0:
        b+=i
if b-a==a:
    print("perfect")
elif b-a<a:
    print("deficient")
else:
    print("abundant")