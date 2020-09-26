import math

# 调用函数
print(abs(-100))


# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-20))


# 空函数
def pop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
xy = move(100, 100, 60, math.pi / 6)
print(x, y)
print(xy)


# 函数的参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))


def calc(numbers):
    summy = 0
    for n in numbers:
        summy = summy + n * n
    return summy


print(calc([1, 2, 3]))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 20, city='Beijing')


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))
