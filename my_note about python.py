

#help(enumerate)
'''enumerate(iterable, start=0)
    enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字
    符串)组合为一个索引序列，同时列出数据和数据下标，一般用在
    for循环当中。
    其中iterable表示可遍历的数据对象(列表，元组，字符串等)，
    start表示索引的起始值，默认为0，一般不需要更改。
    下面写一下例子'''

#第一个例子，遍历列表guns中的每个元素，并输出其索引和元素本身
guns = ['M16', 'AK47', 'M4A1', 'G36C']
#for index, gun in enumerate(guns):
#    print(index, gun)
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
