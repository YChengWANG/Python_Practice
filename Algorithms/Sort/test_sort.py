import random
from All_Sort import *

li = list(range(20))
random.shuffle(li)

heap_sort(li)
print(li)