n = int(input("輸入筆數n:"))
a = int(input("金 "))
b = int(input("銀 "))
c = int(input("銅 "))
d = int(input("優 "))
list1 = [["金",a],["銀",b],["銅",c],["優",d]]
for i in range(n):
    print("%s牌得到%d面"%(list1[i][0],list1[i][1]))