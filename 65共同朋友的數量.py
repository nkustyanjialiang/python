A = list(input("請輸入A的好友:").split())
B = list(input("請輸入B的好友:").split())
sum = 0
for i in A:
    if i in B:
        sum += 1
print(sum)