def a(n): 
    num = []
    while True:
        a = n // 3
        b = n % 3
        num += [str(b)]
        n = a
        if n == 0:
            break
    return ''.join(num[::-1])

while True:
        p=int(input("請輸入十進位的正整數:"))
        print(a(p))
        break