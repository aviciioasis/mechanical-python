import matplotlib.pyplot as plt
'''matplotlib 是一个用于创建可视化图表的 Python 库。它提供了丰富的绘图功能，
可以用来绘制各种类型的图表，如折线图、柱状图、散点图等。
    它通常与 NumPy 和 Pandas 以及scipy等数据处
    理库结合使用，以便更方便地进行数据分析和可视化。
    matplotlib 的主要模块是 pyplot，它提供了
    类似于 MATLAB 的绘图接口，使得用户可以轻松地创建和定制图表。'''

'''在matplotlib中，图表是由多个元素组成的，包括图形（figure）、坐标
轴（axes）、数据点（data points）等。用户可以通过调用不同的函数来创建
和定制这些元素，从而实现各种可视化效果。'''
plt.plot(x,y)'''这是一个用于绘制折线图的函数。'''
plt.scatter(x,y)'''这是一个用于绘制散点图的函数。'''
plt.bar(x,height)'''这是一个用于绘制柱状图的函数。'''
plt.hist(data,bin=10)'''这是一个用于绘制直方图的函数。'''
plt.pie(sizes,labels=labels)'''这是一个用于绘制饼图的函数。'''




'''下面为一个例子，展示了如何使用 matplotlib 绘制一个简单的折线图。'''
plt.figure(figsize=(8, 6))
'''figuresize参数用于设置图表的大小，单位为英寸。figuresize=(8, 6)表
示图表的宽度为8英寸，高度为6英寸。'''

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
'''plt.plot()函数用于绘制折线图。第一个参数是x轴的数据，第二个参数是y轴的数
据，'''


plt.xlabel('X-axis')
'''plt.xlabel()函数用于设置x轴的标签。'''

plt.ylabel('Y-axis')
'''plt.ylabel()函数用于设置y轴的标签。'''

plt.title('My First Plot')
'''plt.title()函数用于设置图表的标题。'''


plt.tight_layout()
'''plt.tight_layout()函数用于自动调整子图参数，使得图表布局
更加紧凑，避免子图之间的重叠。'''


plt.show()
'''plt.show()函数用于显示图表。它会弹出一个窗口，显示绘制的图表。'''