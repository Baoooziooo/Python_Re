'''
    常用匹配规则
'''

import re

# --.点的使用,匹配除了换行符之外的任意一个字符
# data = 'a1aaaa'
# pa = '...' # --匹配规则
# res = re.match(pa,data)
# print(res.group())

# name = '小明','张三','小王','李四'
# paa = '小.' # --匹配规则
# for names in name:
#     res = re.match(paa, names)
#     if res:
#         print(res.group())

# --[]中括号的使用,匹配中括号中的任意一个字符
# data = 'Hello world'
# pa = '[Hel]' # --中括号中的内容,代表一个集合,匹配集合内的任意一个字符
# res = re.match(pa,data)
# print(res.group())

# data = 'a','b','c','e','wyw'
# # pa = '[abc]' # --[abc]代表可以匹配a或b或c
# pa = '[a-z]'
# for datas in data:
#     res = re.match(pa,datas)
#     if res:
#         print(res.group())

# --\d匹配一个数字,0-9
# data = '123456789abcdef'
# pa = '\d'
# res = re.match(pa,data)
# print(res.group())

# --\D匹配一个非数字
# data = 'ad123456789abcdef'
# pa = '\D'
# res = re.match(pa,data)
# print(res.group())

# --\s匹配一个空白或tab键
# data = '  hello'
# print(re.match('\s\s',data).group())

# --\S匹配一个非空白或tab键
# data = 'Python1  hello'
# print(re.match('\S\S\S',data).group())

# --\w匹配单词字符,a-z,A-Z,0-9,_
# data = '_Zyssd12f'
# print(re.match('\w',data).group())

# --\W匹配非单词字符,a-z,A-Z,0-9,_
# data = '@# _Zyssd12f'
# print(re.match('\W\W\W',data).group())