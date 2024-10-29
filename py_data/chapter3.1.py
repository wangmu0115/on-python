tup1 = 1, 2, 3
print(tup1)
tup2 = (4, 5, 6)
print(tup2)
tup3 = tuple(range(5))
print(tup3)
tup4 = tuple("string")
print(tup4[2])
tup5 = (1, 2, 3) + (7, 8, 9)
print(tup5)
tup6 = ("foo", "bar") * 2
print(tup6)
# 1. 交换变量名
a, b = 1, 2
b, a = a, b
print(f"a={a},b={b}")  # a=2,b=1
# 2. 迭代元素是元组的序列
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for x, y, z in seq:
    print(f"x={x},y={y},z={z}")  # x=1,y=2,z=3  x=4,y=5,z=6  x=7,y=8,z=9
# 3. *rest语法丢弃元组中元素
values = 22, 17, 8, 12, 15
m, n, *_ = values
print(f"values[0]={m},values[1]={n}")  # values[0]=22,values[1]=17
