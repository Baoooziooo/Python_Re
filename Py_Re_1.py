import re

data = 'Python is the best language in the world'
# --match只能匹配以xxx开头的字符串,结构是(正则表达式,字符串,附加参数)
# re = re.match('p',data,re.I|re.M) #re.I->不区分大小写
re = re.match('(.*) is (.*?) .*',data,re.I|re.M)
if re:
    print(re)
    print(re.group())
    # --group(num)可以获取匹配数据,多个匹配结果以元组的形式存放到group对象中,通过下标获取
    print(re.group(1))
    print(re.group(2))
    # --groups()是一个元组类型
    print(type(re.groups()))
    pass
else:
    print(re)