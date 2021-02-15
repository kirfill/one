def decorator(f1):
    def ob():
        f1()
        s=(u1*t)+((a*t*t)/2)
        print("расстояние: ",s)
    return ob

@decorator
def f1():
    a = (u2-u1)/t
    print("ускорение: ",a)

try:
    a = 0
    s = 0
    u1 = int(input("u1: "))
    u2 = int(input("u2: "))
    t = float(input("t: "))
    f1()
except ZeroDivisionError:
    print("Ошибка")
except ValueError:
    print("Ошибка")
else:
    print("f")



