#实现一个函数，将1-100内所有的平方数放在一个列表中，如：1,4,9,16~~~~
def list():
    y=1
    list=[]
    for x in range(1,101):
        y=x*x
        if y>100:
            break
        list.append(y)
    return list
print(list())
list1 = [x*x for x in range(1,101)if x*x<=100]
print(list1)
#实现一个函数，通过接受用户的输入字符串，去搜索该字符串是否在固定的字典中，字典的数据需要自己定义。若在该字典中的值就输出
a = input("请输入一个字符串")
def dict():
    dict1 = {'hello': "你好", 'tom': "汤姆",}
    for key,value in dict1.items():
        if a in key:
            return value
print(dict())


