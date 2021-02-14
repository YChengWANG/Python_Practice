string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"

# 默认分割符 ' '
print(string_1.split())
# ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# 自定义分割符 '/'
print(string_2.split('/'))
# ['sample', ' string 2']

print("".join(string_1.split()))