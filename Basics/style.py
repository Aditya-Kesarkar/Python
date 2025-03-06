print("Hello World...!")

# performing addition in scripting style:
a = 10
b = 20
print("Addition of", a, "&", b, "is", a+b)

# procedural style of programming:
def add(c, d):
    print("Addition of c:", c, "& d:", d, "is", c+d)


add(30, 40)

# Object-Oriented style of programming:
class Demo:
    def add(self, c1, d1):
        print("Addition of c1:", c1, "& d1:", d1, "is", c1+d1)

d1 = Demo()
d1.add(50, 60)


# 1. Python is a dynamically typed language in which programmer doesn't need to
#     mention the data-type while declaration!
# 2. Python decides the data-type based on the data stored in the variable!
# 3. Pyhon is the most concise programming language!