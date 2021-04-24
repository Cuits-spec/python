# 字符串查找
str1 = 'hello world and itheima and Python'
# find
print(str1.find('and'))
print(str1.find('and', 15, 30))
print(str1.find('ands'))
# index
print(str1.index('and'))
print(str1.index('and', 15, 30))
# print(str1.index('ands'))  报错
# count
print(str1.count('and'))

# 字符串修改--通过函数形式修改字符串中的数据
str2 = 'hello world and itheima and Python and open'
# replace --替换
# 字符串序列.replace（旧字串，新字串，替换次数）
print(str2.replace('and', 'he'))
print(str2.replace('and', 'he', 1))
# split --分割
# 字符串序列.split（分割字符，分割字符出现的次数+1）
print(str2.split('and'))
print(str2.split('and', 1))
# join --合并字符串
# '合并连接的字符串'.join（多字符组成的序列）
t1 = ['aa', 'bb', 'cc']
new_str = '...'.join(t1)
print(new_str)

# 列表的一个案例
name_list = ['tom', 'jiery', 'cuity']
name = input('请输入你的名字')
if name in name_list:
    print(f"f你输入的名字是{name},她在列表里")
else:
    print(f"f你输入的名字是{name},不存在列表里")