u1 = int(input("u1"))
u2 = int(input("u2"))
t = int(input("t"))



def dekf(f):
     def fg():
         s = t*u1
         print(s)
         f()
     return fg

@dekf
def f():
     a = u2-u1/t
     print(a, "ускорение")

f()



