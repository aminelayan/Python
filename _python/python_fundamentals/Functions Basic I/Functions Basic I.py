#1  prediciton 5
def a():
    return 5
print(a())

#2 prediciton 10
def a():
    return 5
print(a()+a())

#3 prediction 5
def a():
    return 5
    return 10
print(a())

#4 predicition 5
def a():
    return 5
    print(10)
print(a())

#5 predcition Nothing,null
def a():
    print(5)
x = a()
print(x)

#6 prediction 3 5 Error
def a(b,c):
    print(b+c)
# print(a(1,2) + a(2,3))

#7 prediciton 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 predcition 100 10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 predcitions 7 14 7+14=21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 prediciton 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 predicition 500 500 300 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 predicition 500 500 300 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#14 prediction 1 3 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()


# 15 prediciton 1,3,5,10
def a():
    print(1)
    x=b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y=a()
print(y)