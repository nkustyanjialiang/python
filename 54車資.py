a=float(input("請輸入路程公里數(km):"))
if a<=1.5:
    print("所需車資為:75")
else:
    import math
    b=(a-1.5)*1000/250
    c=math.ceil(b)*5
    print("所需車資為:",75+c)