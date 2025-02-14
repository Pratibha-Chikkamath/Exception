class Grandmother:
    def m1(self):
        print("grandmother cook old tasty food")
class Mother(Grandmother):
    def m2(self):
        print("mother cooks tasty food")
class Douther(Mother):
    def m3(self):
        print("eat tasty food")

d=Douther()
d.m1()
d.m2()
d.m3()