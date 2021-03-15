# 常用的5个标准库
import os
import sys
import re
import math
import datetime

#numpy
import numpy as np 

#iter
li = [1,2,3,4]
for i in li:
    print(i,end='')

# global
a = 4

def func():
    global a
    a = 5


func()
print(a)

map_res = map(lambda x: x**2 ,[x for x in range(10)])
print([x for x in map_res if x >50])

#random
random_number = np.random.randn(5)
print(random_number)