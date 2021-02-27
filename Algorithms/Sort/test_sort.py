from All_Sort import *
import copy
import random

li = list(range(1000))
random.shuffle(li)
#print(li)
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
li3 = copy.deepcopy(li)
li4 = copy.deepcopy(li)
li5 = copy.deepcopy(li)

bubble_sort(li1)
select_sort(li2)
insert_sort(li3)
quick_sort(li4)
heap_sort(li5)