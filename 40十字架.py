a=int(input("輸入整數n:"))
c=""
for i in range(1,a,2):
    print(end="    ")
    print(i)
for i in range(1,a+1,2):
    c=c+str(i)
for i in range((a-2),0,-2):
    c=c+str(i)
print(c)
for i in range((a-2),0,-2):
    print(end="    ")
    print(i)