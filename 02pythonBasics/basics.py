# 字符类型和变量
print('包含中文的字符串')

# 字符串和编码
print('Hi, %s, you have $%d.' % ('Michael', 10000));
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0},成绩提升了 {1:.1}%'.format('小明', '17.25'))

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# 使用list和tuple
classmates = ['AA', 'BB', 'CC']
print(classmates)
print(len(classmates))

classmates = ('AAA', 'BBB', 'CCC')
print(classmates)
t = ('a', 'b', ['c', 'd'])
t[2][0] = 'x'
t[2][1] = 'y'
print(t)

# 条件判断
age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')
else:
    print('teenager')

# 循环
names = ['AA', 'BB', 'CC']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 使用dict和set
dict = {'A': 90, 'B': 80, 'c': 70}
print(dict['B'])

s = set([1, 2, 3])
print(s)
