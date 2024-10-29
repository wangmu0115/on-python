## 元组

**长度固定且不可变的 Python 序列对象**，以逗号 `,` 分割序列值，元组序列开始和结束的圆括号 `()` 可以省略。

- `tuple()`方法可以将任意序列或迭代器转换成元组。
- 通过方括号 `[]` 和序列索引（从`0`开始）可以访问元组中的元素。
- `+`运算符可以将多个元组串联起来形成更长的元组。
- `*`运算符可以复制元组并串联起来。
- `tuple.count($item)`：元组的实例方法`count()`可以统计某个值出现的频次。

### 元组拆包

```python
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
```