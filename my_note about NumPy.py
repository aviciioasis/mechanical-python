import numpy as np    
''' numpy 是一个工具，
它是python的一个拓展程序库，支持大量的维度
数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。  
    numpy主要用于数组计算。    
    np为我个人定义的简写，方便调用函数。
'''





#help(np.linspace)
'''np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    np.linspace()函数返回在指定的间隔内均匀间隔的数字。
    其中start和stop是指定的间隔范围（即定义域），
    num是指定的样本数，
    endpoint表示是否包含stop值（若未标注则默认为True），
    retstep表示是否返回间距，
    dtype表示数据类型，
    axis表示沿着哪个轴进行操作。(上述例子中为第一个轴)
    下面写几个例子'''

#第一个例子
#np.linspace(0, 10, 10)
#print(np.linspace(1, 10, 10,))
'''该例子输出结果为[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
即从1开始到10结束，输出10个数，包含10，每个数之间的间隔相等，且为1'''

#第二个例子
#np.linspace(0, 10, 10,endpoint=False) 
#print(np.linspace(1, 10, 10,endpoint=False))
'''该例子输出结果为[1.  1.9 2.8 3.7 4.6 5.5 6.4 7.3 8.2 9.1]
即从1开始到10结束，输出10个数，不包含10，每个数之间的间隔相等，且为0.9'''





#help(np.zeros)
'''np.zeros(shape, dtype=float, order='C',device=None, like=None)
    np.zeros()函数返回一个给定形状和类型的用0填充的新数组。
    其中shape表示数组的形状[元组形式，一般为(行row, 列column)]，
    dtype表示数据类型(int整数,float浮点数之类的，细分的类型再查表)，
    order表示数组的存储顺序,只有'C'和'F'两种选择，
    其中C为行优先，即按行存储数据（默认，为横向），F为列优先，即按列存储数据。
    device表示设备，用于指定数据在哪个设备上运行，一般只有CPU，
    like表示类似的对象，这是 NumPy 的 Array Function 协议的入口。
    如果你传入的是 CuPy 数组、JAX 数组等支持 __array_function__ 的
    第三方数组，np.zeros 会自动调用对应库的实现，返回该库类型的数组，
    下面写一下例子
'''

#第一个例子
#np.zeros((3, 4), dtype=int)
#print(np.zeros((3, 4), dtype=int))
'''该例子输出结果为：
[[0 0 0 0] 
 [0 0 0 0] 
 [0 0 0 0]]
 即生成一个3行4列的二维数组，且数据类型为整数，所有元素均为0'''




help(np.random)
'''该函数为numpy库中的随机数生成模块，提供了多种随机数生成方法，
包括均匀分布、正态分布、二项分布等。但调用接口分为新版和旧版，下面做说明：
新版API：


旧版API（整个程序共享一个全局随机状态）：
1. np.random.rand(d0, d1, ..., dn)：生成[0, 1)范围内的均匀分布随机数，参数为生成数组的形状。
2. np.random.randn(d0, d1, ..., dn)：生成标准正态分布（均值为0，标准差为1）的随机数，参数为生成数组的形状。
3. np.random.randint(low, high=None, size=None, dtype=int)：生成指定范围内的整数随机数，参数包括下限、上限、生成数量和数据类型。
4. np.random.choice(a, size=None, replace=True, p=None)：从给定的一维数组中随机抽取指定数量的元素，参数包括数组、生成数量、是否可重复抽取和概率分布。
5. np.random.shuffle(x)：对给定的一维数组进行随机排列，参数为要排列的数组。'''

help(np.random.normal)
'''该函数用于生成符合正态分布的随机数。它的参数包括：
loc: 正态分布的均值（mean），默认为0，（确定基础）。
scale: 正态分布的标准差（standard deviation），默认为1，（可自定义其数值和标准）。
size: 输出的随机数的形状（shape），可以是整数（多少个随机数）或元组（数组类型dimensions），默认为1。
返回值为一个ndarray对象，包含生成的随机数。
下面写一下例子'''