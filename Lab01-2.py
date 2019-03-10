print("1-100中奇数有：")
for i in range(1, 101):
    if i % 2 == 1:
        print("%3d" % i,end=" ")
    i = i + 1
