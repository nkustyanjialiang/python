a = int(input("請輸入電費度數:"))

if a <= 120:
    print("Summer months:",(a*2.10))
    print("Non-Summer months:",(a*2.10))
elif a <=330:
    print("Summer months:",(a-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(a-120)*2.68 + 120*2.10)
elif a <=500:
    print("Summer months:",(a-330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(a-330)*3.61 + (330-120)*2.68 + 120*2.10)
elif a <=700:
    print("Summer months:",(a-500)*4.97 + (500-330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(a-500)*4.01 + (500-330)*3.61 + (330-120)*2.68 + 120*2.10)
elif a >700 :
    print("Summer months:",(a-700)*5.63 + (700-500)*4.97 + (500-330)*4.39 + (330-120)*3.02 + 120*2.10)
    print("Non-Summer months:",(a-700)*4.50 + (700-500)*4.01 + (500-330)*3.61 + (330-120)*2.68 + 120*2.10)