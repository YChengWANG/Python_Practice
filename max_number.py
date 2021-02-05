def Max_number(num):
    str_num = str(abs(num))
    if(num>=0): 
        for i in range(len(str_num)):
            if str_num[i]<="5":
                return int(str_num[:i]+"5"+str_num[i:])
    else:
        for i in range(len(str_num)):
            if str_num[i]>="5":
                return -int(str_num[:i]+"5"+str_num[i:])
    return int(str_num+"5")


num = -999
res = Max_number(num)
print(res)