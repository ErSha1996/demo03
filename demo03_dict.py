#字典的定义
dict = {'a':1,'b':'hello','c':[1,2,3],'d':False}
print(dict)
print()
# 查询字典中某个键所对应的值
print(dict['a'])
print(dict.get('a'))
print()
# 查询字典中所有的值
print(dict.values())
for x in dict.values():
    print(x,end=" ")
print()
print()
# 获取所有的健
print(dict.keys())
for y in dict.keys():
    print(y,end=" ")
print()
print()
# 查询字典中所有的键值对
print(dict.items())
for z in dict.items():
    print(z,end="")
print()
print()
# 字典的更新
dict1 ={'e':'python','f':'java'}
dict.update(dict1)
print(dict1)
print(dict)
print()
print()
# 删除对应的键值对
dict.pop('e')
print(dict)
print()
print()
# 删除最后一个键值对
dict.popitem()
print(dict)
print()
print()
# 清空
dict1.clear()
print(dict1)
