class SquareRoot:
    def __init__(self, num):
        self.num = num
    def square_root(num):
        g = num/2
        i = 0
        while abs(g**3 - num) > 0.00000000001:
            g = (2*g)/3 + num/(3*(g**2)) #开三次方根的公式
            i = i + 1
        print("% .13f" % g)
a = input("请输入一个数：")
SquareRoot.square_root(int(a))