



help(enumerate)
'''enumerate(iterable, start=0)
    enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字
    符串)组合为一个索引序列，同时列出数据和数据下标，一般用在
    for循环当中。
    其中iterable表示可遍历的数据对象(列表，元组，字符串等)，
    start表示索引的起始值，默认为0，一般不需要更改。
    下面写一下例子'''

#第一个例子，遍历列表guns中的每个元素，并输出其索引和元素本身
guns = ['M16', 'AK47', 'M4A1', 'G36C']
for index, gun in enumerate(guns):
    print(index, gun)
'''该例子输出结果为：
0 M16
1 AK47
2 M4A1
3 G36C 
即输出了列表guns中每个元素的索引和元素本身'''

#第二个例子，遍历列表guns中的每个元素，指定索引起始值，
#并输出其索引和元素本身，从索引1开始。
for index, gun in enumerate(guns, start=1):
    print(index, gun)
'''该例子输出结果为：
1 M16
2 AK47
3 M4A1
4 G36C 
即输出了列表guns中每个元素的索引和元素本身，索引从1开始'''

#第三个例子，转换成列表或者词典形式，输出
enumerate_list = list(enumerate(guns))
print(enumerate_list)
'''该例子输出结果为：
[(0, 'M16'), (1, 'AK47'), (2, 'M4A1'), (3, 'G36C')]
即输出了列表guns中每个元素的索引和元素本身，以元组形式存储在列表中'''

enumerate_dict = dict(enumerate(guns))
print(enumerate_dict)
'''该例子输出结果为：
{0: 'M16', 1: 'AK47', 2: 'M4A1', 3: 'G36C'}
即输出了列表guns中每个元素的索引和元素本身，以字典形式存储'''

#第四个例子，遍历字符串s中的每个字符，并输出其索引和字符本身
s = 'Hello, World!'
for index, char in enumerate(s):
    print(index, char)
'''该例子输出结果为：
0 H
1 e
2 l
3 l
4 o
5 ,
6  
7 W
8 o
9 r
10 l
11 d
12 !
即输出了字符串s中每个字符的索引和字符本身'''






help(dict(key, value))
'''dict()函数用于创建一个字典对象。
    其中key表示键，value表示值，键值对之间用冒号分隔，多个键值对之间用逗号分隔。
    需要注意的是，dict()函数创建的字典对象是无序的，即键值对的顺序是不固定的。
    花括号{}表示字典对象，键值对之间用冒号分隔，多个键值对之间用逗号分隔。
    如{'key1':10, 'key2':20}等；
    而小括号（）表示元组对象，需要使用=进行赋值。
    下面写一下例子'''





dict(key=10, value=20)
print(dict(key=10, value=20))
'''该例子输出结果为：
{'key': 10, 'value': 20}
即创建了一个字典对象，键为'key'，值为10，键为'value'，值为20。'''



dict1 = {'a': 1, 'b': 2, 'c': 3}
for index, (key, value) in enumerate(dict1.items()):
    print(index, key, value)
'''该例子输出结果为：
0 a 1
1 b 2
2 c 3
即输出了字典dict1中每个键值对的索引(0, 1, 2)、键(a, b, c)和
值(1, 2, 3)'''


dict2={'x': 10, 'y': 20, 'z': 30}
for index, (key, value) in enumerate(dict2.items(), start=1):
    print(index, key, value)
'''该例子输出结果为：
1 x 10
2 y 20
3 z 30
即输出了字典dict2中每个键值对的索引(1, 2, 3)、键(x, y, z)和
值(10, 20, 30)'''



dict.items()
'''dict.items()方法用于返回字典中的所有键值对，以元组的形式返回。
    其中dict表示字典对象(可以是任何字典，包括自己编写的字典如前面的dict1, dict2等)，
    items()方法返回一个包含所有键值对的视图对象，每个键值对以元组的形式表示，元组的
    第一个元素是键，第二个元素是值。
    需要注意的是，dict.items()方法返回的视图对象是动态的，即当字典发生
    变化时，视图对象也会随之变化。
    下面写一下例子'''

dict3 = {'name': 'Alice', 'age': 25, 'gender': 'female'}
for index, (key, value) in enumerate(dict3.items()):
    print(index, key, value)
'''该例子输出结果为：
0 name Alice
1 age 25
2 gender female
上面的输出表明：输出了字典dict3中每个键值对的索引(0, 1, 2)、
键(name, age, gender)和后面的值(Alice, 25, female)'''










filename=f'{dict3["name"]}_data of persons.csv'
print(filename)
'''该例子输出结果为：
'filename'变量的值为'Alice_data of persons.csv'，即将字典
dict3中键'name'对应的值'Alice'与字符串'_data of persons.csv'拼接起来，形成了一
个新的字符串，并赋值给变量'filename'。

需要注意的是，f-string是一种格式化字符串的方式，可以在字符串中嵌入变量或表达式，
通过在字符串前加上字母'f'，并使用花括号{}将变量或表达式括起来，即可实现字符串的
格式化输出。'''    



import pandas as pd
df = pd.DataFrame([dict3])
df.to_csv(filename,index=False,encoding='utf-8-sig')
print(f'{filename}已保存为csv文件')
'''该例子输出结果为：
'Alice_data of persons.csv已保存为csv文件'，即将字典dict3转换为DataFrame对象，
并保存为csv文件，文件名为'Alice_data of persons.csv'，不包含索引，编码格式为'utf-8-sig'。
需要注意的是，pandas是一个强大的数据分析库，可以方便地进行数据处理和分析，
DataFrame是pandas中最常用的数据结构之一，可以看作是一个表格型的数据结构，类似于Excel表格。
to_csv()方法用于将DataFrame对象保存为csv文件。
输出的文件已经保留在当前工作目录下，可以使用os模块查看当前工作目录。
详细的部分在practice.ipynb中展示，需自行配置好python环境和pandas库。'''   