numpy.arange()

%timeit

N维数组对象，ndarray，同构数据多维容器
同构指的是数组元素的类型相同
ndim: 数组的维度，是个标量
shape: 各维度大小的元组
dtype: 数组元素类型

创建ndarray

np.array()，接收任意序列型对象，返回一个新的包含输入数据的NumPy数组
np.array([[1.5, -0.1, 3], [0, -3, 6.5]])