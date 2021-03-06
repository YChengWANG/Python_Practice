dic = {'a':24, 'g':52, 'i':33, 'k':12}

dic_sorted = sorted(dic.items(), key= lambda x: x[1])
print(dic_sorted)

lists = [{'name':'james','age':20},{'name':'ball','age':30},{'name':'mike','age':25}]
lists_sorted = sorted(lists, key= lambda x: x['name'],reverse=True)
print(lists_sorted)