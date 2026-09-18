import pandas as pd 
'''pandas是一个开源的Python扩展程序库，也是一个数据分析库，
它提供了高性能、易用的数据结构和数据分析工具。
    pandas主要用于数据分析，
pandas的核心数据结构是DataFrame（多维表格）和Series（一维数组）。'''





#pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
'''pd.DataFrame()函数用于创建一个DataFrame对象。
    其中data表示数据，可以是ndarray、Series、map、lists、dict等类型的数据；
    index表示索引，可以是单个标签或标签列表，默认为None；
    columns表示列标签，可以是单个标签或标签列表，默认为None；
    dtype表示数据类型，默认为None；
    copy表示是否复制数据，默认为False。
    下面是一个创建DataFrame对象的示例：'''

pd.DataFrame(data={'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
print(pd.DataFrame(data={'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c']))
'''该例子输出结果为：
   A  B
a  1  4
b  2  5
c  3  6
即创建了一个3行2列的DataFrame对象，行索引为'a'、'b'、'c'，
列标签为'A'、'B'，数据分别为1、2、3和4、5、6。'''

pd.DataFrame({
        '位移_mm': displacement_mm,
        '力_kN': force_kn,
        '应变': strain,
        '应力_MPa': stress,
        '材料': name
    })
'''此时，创建了一个DataFrame对象，第一列为名称，第二列为数据。
第一列包含5列数据，分别为：位移_mm、力_kN、应变、应力_MPa和材料，
第二列为具体数值，每列数据的类型分别为float64、float64、float64、float64和object。'''    