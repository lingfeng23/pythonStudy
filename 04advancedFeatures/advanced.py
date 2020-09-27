from collections.abc import Iterable

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
# 切片
L = ['A', 'B', 'C', 'D', 'E']

print(L[0:3])
L = list(range(100))
print(L)
print(L[:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[:10:2])  # [0, 2, 4, 6, 8]
# 迭代
print(isinstance('abc', Iterable));

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 列表生成式
print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]
print([m + n for m in 'ABC' for n in 'XYZ'])  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
# 生成器
generator = (x * x for x in range(10))
for n in generator:
    print(n)
# 迭代器
"""
可以直接作用于for循环的数据类型有以下几种：
    一类是集合数据类型，如list、tuple、dict、set、str等；
    一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
"""