import re

# data = re.search("\w", "abas13s")
# print(data.group())
# print(data.groups())  # 返回括号的内容

data = re.search("(<b>(?P<b>.*?)</b>)", "<b>b标签</b>")
# print(data.group())
# print(data.group(0))
# print(data.group(1))
# print(data.group(2))
print(data.group('b'))
print(data.groups())  # 返回括号的内容