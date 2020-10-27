# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random 
n=1
r=random.randint(0,100)#生成0-100的一个随机整数#
b=input("请输入0到100内的一个整数")
c=int(b)#用户输入一个整数#

while c!=r :    # //此循环条件可以优化一下。另外，变量要用有意的单词命名
    if c<r:
        print("猜小了，请再猜一次")
        b=input("请输入0到100内的一个整数")    # 不需要在两个判断中都输入
        c=int(b)
    elif c>r:
        print("猜大了，请再猜一次")
        b=input("请输入0到100内的一个整数")
        c=int(b) 
    n=n+1    
print("猜对了！一共猜了{}次".format(n))
