animals=['rat','ox','tiger','rabbit','dragon','snake','horse','sheep','monkey','rooster','dog','pig']
a=int(input('請輸入出生西元年份:'))
b=a-4
if b>=12:
    c=b%12
else:
    c=b
print(animals[c])