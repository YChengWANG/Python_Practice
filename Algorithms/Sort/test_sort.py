from All_Sort import *
import copy
import random

li = list(range(20))
random.shuffle(li)
#print(li)

heap_sort(li)
print(li)