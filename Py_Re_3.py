'''
    限定匹配字符的数量
'''

import re
# --*号匹配前一个字符出现0次或者无限次,即可有可无
# print(re.match('[A-Z][A-Z]*','My').group())
# print(re.match('[A-Z][a-z]*','Any').group())
# print(re.match('[A-Z][a-z]*','AnyeverDayhappy').group())

# --+号匹配前一个字符出现1次或者无限次,至少有1次
# print(re.match('[a-zA-Z]+','MYNameis').group())
# --匹配符号规范的python变量名,规则:不能以数字开头,只能包含字母,数字,下划线
# print(re.match('[a-zA-Z_]+[\w]*','_name').group())

# --\?号,? 匹配前导字符0次或者1次,表示前导字符可以选择
# print(re.match('[a-zA-Z]+[0-9]?','nnnnFu3a99me').group())

# --{min,max}匹配前导字符min次到max次,min和max必须是非负数
# --{count}表示精确匹配
# print(re.match('\d{4}','1234').group())
# --{min,}表示max没有限制,{,max}表示min没限制
# print(re.match('\d{4,}','1234567890').group())
# --{min,max}表示max没有限制
# print(re.match('\d{3,6}','1234567890').group())
# --匹配邮箱,格式:xxxxx@xxx.com
# print(re.match('\w+@.+\.com','zs255555zx@163.com').group())
# print(re.match('\w{6,11}@.+\.com','zs255555zx@163.com').group())

# --转义
# print(re.match('c:\\\\a.txt','c:\\a.txt').group())
# print(re.match(r'c:\\a.txt','c:\\a.txt').group()) # --在正则前面+r表示原生字符串,python解释器就不会转义了

# --^匹配字符串开头
# print(re.match('^P\w{5}','Python is langage').group())

# --$匹配字符串结尾
# print(re.match('.*age$','Python is langage').group())