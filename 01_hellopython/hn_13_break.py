# 当while循环遇见break，会直接退出循环

i = 0
while i < 10:

    if i == 3:
        break
    print(i)
    i += 1

print("over")