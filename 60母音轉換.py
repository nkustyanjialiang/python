list = ["a","e","i","o","u"]
english = input("請輸入一串小寫英文：")
for i in range(len(list)):
    english = english.replace(list[i],".")
print(english)