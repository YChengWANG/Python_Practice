# 常用的5个标准库
import os
import sys
import re
import math
import datetime

#re
print(p.search('zy3t4r1').group())

# global
a = 4

def func():
    global a
    a = 5


func()
print(a)