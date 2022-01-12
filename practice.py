# 输入a,b,c,d 4个整数，计算a+b-c*d的结果
# a = 1
# b = 2
# c = 3
# d = 4
# x = a+b
# y = c*d
# z = x-y
# print (x)
# print (y)
# print (z)
# a = input("请输入1个数:")
# b = input("请输入1个数:")
# c = input("请输入1个数:")
# d = input("请输入1个数:")
# print(int(a)+int(b)-int(c)*int(d))

# 打印1-100以内被3整除的所有数的和
# a = 3
# b = 3
# sum = 0
# c = b%a
# while c==0 and b<=100:
#     sum += b
#     b += 3
# print(sum)
# 使用range（）输出1-10以内的所有数字、输出所有奇数
# for x in range(1,11,1):
#     print(x)
# for y in range(1,11,2):
#     print(y)
# 打印1-100所有偶数的和减去所有奇数的和的值
# sum = 0
# sum1 = 1
# for g in range(0,101,2):
#     sum += g
# for h in range(1,101,2):
#     sum1 += h
# print(sum - sum1)
#求1+2+3+...+100的和
# sum = 0
# for d in range (1,101,1):
#     sum += d
# print(sum)
# 判断一个数n能同时被3和5整除
# n = 0
# f = n%3
# g = n%5
# if f == 0 and g == 0:
#     n += 1
# print('true')
#
# n = input("请输入一个整数:")
# if int(n) % 3 == 0 and int (n) % 5 == 0:
#     print("{}能被3和5整除".format(n))
# else:
#     print("{}不能被3和5整除".format(n))
# 定义一个整数变量，判断该变量值是否是1-100以内的某个数，如果是就打印出来
# e = 0
# while e <= 99 and e >= 0:
#     e += 1
#     print(e)
#输入三个数x,y,z,请把这三个数由小到大输出。备注：输入方法：input()
# lst = []
# x = input("输入第一个数:")
# y = input("输入第二个数:")
# z = input("输入第三个数:")
# lst.append(int(x))
# lst.append(int(y))
# lst.append(int(z))
# lst.sort()
# print(lst)
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
# score = input("输入一个整数：")
# if 90<=int(score)<=100:
#     print("A")
# elif 60<=int(score)<=89:
#     print("B")
# elif int(score)<60:
#     print("C")
#将一个列表的数据复制到另一个列表中
lst1 =[2,3,4,5]

lst2 =lst1.copy()
print(lst2)

lst3 = lst1
print(lst3)

lst4 = []
for h in lst1:
    lst4.append(h)
print(lst4)
#输出9*9乘法口诀表
for i in range(1,10):
    for j in range(i,10):
        print("{}*{}={}".format(i,j,i*j),end="")
    print()
#输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数
alpha = 0
digit = 0
space = 0
other = 0
k = input("请输入一个字符串:")
for l in k:
    if str(l).isalpha():
        alpha += 1
    elif str(l).isdigit():
        digit += 1
    elif str(l).isspace():
        space += 1
    else:
        other += 1
print("字母:{alpha},数字:{digit},空格:{space},其他:{other}".format(alpha=alpha,digit=digit,space=space,other=other))
#求s=a+aa+aaa+aaaa+a...a的值，其中a是一个数字，有几个数字由键盘控制
