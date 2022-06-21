a=int(input("輸入a的係數"))
b=int(input("輸入b的係數"))
c=int(input("輸入c的係數"))
x=(-b+(b**2-4*a*c)**0.5)/2*a
y=(-b-((b**2-4*a*c)**0.5))/2*a
d=b**2-4*a*c
if (d==0):
    print(x)
elif(d<0):
    print("0")    
else:
    print(x,y)