import re
'''
修正符 也就是第三个参数
re.S   使.可以匹配换行符  也就是.*?  是无敌的了
re.I   匹配不区分大小写
'''
myStr = """
<a href="http://www.baidu.com">百度</a>
<a href="http://www.taobao.com">淘宝</a>
<A href="http://www.taobao.com">淘宝2</A>
<a href="http://www.aiqiyi.com">爱奇
艺</a>
"""


data = re.finditer('<a href=".*?">.*?</a>', myStr, re.I|re.S)
# data = re.findall('<a href=".*?">.*?</a>', myStr, re.I|re.S)
# print(data)
for i in data:
    print(i.group())  # 获取值