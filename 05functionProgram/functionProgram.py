"""高阶函数"""
# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
f = abs;
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# map两个参数，一个是函数，一个是Iterable
def f(x):
    return x * x;


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(r))

# reduce把一个函数作用在一个序列上
from functools import reduce


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


print(reduce(add, [1, 3, 5, 7, 9]))
print(reduce(fn, [1, 3, 5, 7, 9]))


# filter用于过滤序列
def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

# sorted对list进行排序
print(sorted([36, 23, -12, 38, -28]))
print(sorted([36, 23, -12, 38, -28], key=abs))
"""返回函数"""
