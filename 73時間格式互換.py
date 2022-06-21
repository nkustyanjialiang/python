def a(t):
    h,m,s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
while True:
  x=int(input("請輸入時間1(時:分:秒)2(秒):"))
  if(x==2):
      y=int(input("請輸入時間2(秒):"))
      m, s = divmod(y, 60)
      h, m = divmod(m, 60)
      print ("%02d:%02d:%02d" % (h, m, s))
      continue
  else:
      z=str(input("請輸入時間1(時:分:秒):"))
      print(a(z))
      break