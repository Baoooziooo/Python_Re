'''
    正则表达式对象
'''
import re

# --compile,re模块中的编译方法,把字符串编译成一个字节码,字节码就是一个正则表达式对象
# --优点:在使用正则表达式进行match的操作时,python会将字符串转换成正则表达式对象,如果使用compile则只需要完成一次转换即可,后在使用模式对象无需重复转换
# --创建对象
# reco = re.compile('\d{4}')
# --使用对象
# re = reco.match('12345678')
# print(re.group())

# --search,在全文中匹配一次,匹配到就返回
# data = '我爱伟大的祖国,I love China,China is a great country'
# re = re.search('China',data)
# print(re)
# print(re.group())

# --findall,匹配所有返回一个列表
# data = '啊华为是华人的骄傲,华侨哈哈哈'
# re = re.findall('华.',data)
# rese = re.search('华.',data)
# print(re)
# print(rese.group())
# --使用compile
# reo = re.compile('华.')
# print(reo.search(data).group())
# print(reo.findall(data))

# --sub,将匹配到的数据进行替换
# --subn,返回被替换的数量
# data = 'hello world'
# reo = re.sub('h','H',data)
# print(reo)
# data = 'Pythons是比较受欢迎的编程语言'
# pat = '[a-zA-Z]+'
# res = re.sub(pat,'C++',data)
# resn = re.subn(pat,'C++',data)
# print(res)
# print(resn)

# --split,分割字符串
# data = '百度,腾讯,阿里,华为,360'
# print(re.split(',',data))