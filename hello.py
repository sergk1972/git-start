def summary(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    return z

def devine(x, y):
    if y != 0:
        return x/y
    else:
        print("0 is forbidden!")

print(x:="Hello World!")
print(y:="Work hard!")
print(f"{y} and {x}")
lst2 = list(y)
lst2.pop()
print(lst2)
lst1 = list(x)
lst1.pop()
print(lst1)
