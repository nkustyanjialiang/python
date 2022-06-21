con=["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio","Sagittarius","Capricornus" ]
month=int(input("請輸入出生月份:"))
day=int(input("請輸入出生日期:"))
if month==1:
    if day<20:
        print("星座為:",con[11])
    else:
        print("星座為:",con[0])
elif month==2: 
    if day<19:
        print("星座為:",con[0])
    else:
        print("星座為:",con[1])
elif month==3:
    if day<20:
        print("星座為:",con[1])
    else:
        print("星座為:",con[2])
elif month==4:
    if day<20:
        print("星座為:",con[2])
    else:
        print("星座為:",con[3])
elif month==5:
    if day<21:
        print("星座為:",con[3])
    else:
        print("星座為:",con[4])
elif month==6:
    if day<21:
        print("星座為:",con[4])
    else:
        print("星座為:",con[5])
elif month==7:
    if day<22:
        print("星座為:",con[5])
    else:
        print("星座為:",con[6])
elif month==8:
    if day<23:
        print("星座為:",con[6])
    else:
        print("星座為:",con[7])
elif month==9:
    if day<23:
        print("星座為:",con[7])
    else:
        print("星座為:",con[8])
elif month==10:
    if day<23:
        print("星座為:",con[8])
    else:
        print("星座為:",con[9])
elif month==11:
    if day<22:
        print("星座為:",con[9])
    else:
        print("星座為:",con[10])
elif month==12:
    if day<22:
        print("星座為:",con[10])
    else:
        print("星座為:",con[11])