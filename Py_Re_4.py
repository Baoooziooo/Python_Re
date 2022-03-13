'''
    分组匹配
'''
import re

# --| 匹配左右任意一个表达式,或的关系
# print(re.match('(abc|123)','abc123').group())
# --匹配电话号码 xxxx-12345678910
# print(re.match('([\d]*)-(\d*)','0912-12356482').group())
# --此处 ^ 表示取反,取不是-的字符
# print(re.match('([^-]*)-(\d*)','0912-12356482').group())

# --\num的使用,引用分组
# htmltag = '<html><h1>数据测试</h1></html>'
# re = re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmltag)
# print(re.group())
# print(re.group(1))
# print(re.group(2))
# print(re.group(3))

# --分组别名,(?P<名字>正则),引用(?P=名字)
# data = '<div><h1>www.baidu.com</h1></div>'
# re = re.match(r'<(\w*)><(\w*)>.*</\w*></\w*>',data)
# re = re.match(r'<(?P<div>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=div)>',data)
# print(re.group())