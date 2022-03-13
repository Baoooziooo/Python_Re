'''
    贪婪模式,非贪婪模式
'''
import re

# --贪婪模式,尽可能多匹配结果
# data = 'a22222'
# print(re.match('.*\d',data).group())

# --非贪婪模式,尽可能少的去匹配结果
# data = 'a11111'
# print(re.match('.*?\d',data).group())

# --例子,贪婪模式
# con = 'aaabbbcdbcdc'
# pa = re.compile('a.*b')
# re = pa.search(con)
# print(re.group())

# --例子,非贪婪模式
# con = 'aaabbbcdbcdc'
# pa = re.compile('a.*?b')
# re = pa.search(con)
# print(re.group())