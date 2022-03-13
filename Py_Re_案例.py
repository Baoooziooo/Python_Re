'''
    小结
    1.元字符
        \d,匹配任意单个数字 0-9
        \D,匹配任意单个非数字 A/a
        \w,匹配任意单个数字,字母,_ aA-zZ,0-9,_
        \W,匹配任意单个非\w字符 @#$%
        \s,匹配单个空格
        \S,匹配单个非空格
        \n,匹配换行符
        .,匹配任意单个字符,换行符除外
        \num,匹配前面引用的分组,见文件4案例
    2.多次重复匹配
        A{3},精准N次匹配 AAA
        A{3,},最少出现3次 AAA
        \d{3,5},约定出现最少和最大次数
        \d*,出现0次到无限次
        \d+,最少出现一次
        \d?,最多出现一次={0,1}
    3.定位匹配
        ^A.*,^头匹配
        A.*$,$尾匹配
        ^A.*$,全字匹配
    4.字符范围匹配
        A,精准匹配
        x|y,运行匹配左右两边字符
        [xyz],字符集合允许出现集合内任意单个字符
        [a-z][A-Z][0-9],字符范围
        [^xyz][^0-9],相当于取反(非),集合内字符不允许出现
'''
import re

# --1.长度为8-10的用户密码(以字母开头,包含字母,数字,下划线)
# recom = re.compile('[a-zA-Z]\w{7,10}$')
# re = recom.match('abcdefga')
# if re:
#     print('密码是:{}'.format(re.group()))
# else:
#     print('密码式错误,正确格式为:字母开头,长度为8-10位')

# --2.验证用户名,长度为6-18位的英文字母组成
# recom = re.compile('[a-zA-Z]{5,18}$')
# res = recom.match('aaaaaaaaaaaaaaaaaaa')
# if res:
#     print('用户名:{}'.format(res.group()))
# else:
#     print('用户名格式错误,正确格式为6-18位的英文字母组成')

# --3.邮箱验证126,163邮箱:6-18个字符,可以使用字母,数字,下划线,字母开头
# recom = re.compile('[a-zA-z]\w{5,18}@(126|163)\.com')
# res = recom.match('a1234_a5789456123fj@126.com')
# if res:
#     print('邮箱:{}'.format(res.group()))

# --4.匹配手机号码(11位数字),并区分是那个运营商
# recom = re.compile('([0-9]{3})([0-9]{8})')
# res = recom.match('15144886403')
# if res:
#     BJres = int(res.group(1))
#     if BJres >= 134 and BJres <= 139 or BJres >= 150 and BJres <= 152 or BJres >= 157 and BJres <= 159 or BJres == 182 or BJres == 183 or BJres == 187 or BJres == 188 or BJres == 147:
#         print('号码:{}是移动运营商'.format(res.group()))
#     elif BJres >= 130 and BJres <= 132 or BJres == 136 or BJres == 185 or BJres == 186 or BJres == 145:
#         print('号码:{}是联通运营商'.format(res.group()))
#     elif BJres == 133 or BJres == 153 or BJres == 180 or BJres == 189:
#         print('号码:{}是电信运营商'.format(res.group()))

# --5.'Save your heart for someone who cares'使用正则将文本中的"s"替换成"S"
# recom = re.compile('s')
# res = recom.sub('S','Save your heart for someone who cares')
# print(res)

# --6.'<span>三生三世,十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>',使用正则将<span>标签中的内容全部匹配出来
# recom = re.compile(r'<span>(.*)</span><span>(.*)</span><span>(.*)</span>')
# recom = re.compile(r'<(?P<a>\w*)>(.*)</(?P=a)><(?P=a)>(.*)</(?P=a)><(?P=a)>(.*)</(?P=a)>')
# recom = re.compile(r'<(.*?)>(.*?)<(/.*?)>')
# recom = re.compile(r'<span>(.*?)</span>')
# recom = re.compile(r'<(?P<a>.*)>(.*?)</(?P=a)>')
# res = recom.findall('<span>三生三世,十里桃花</span><span>九州海上牧云记</span><span>莫斯科行动</span>')
# print(res)
