import re

# 按照数字拆分
# print(re.split('\d', 'abc1dcb2vv'))
# print(re.split('[a-zA-Z]', 'abc1dcb2vv'))
# print(re.split('\s', 'abc\r1dc\nb2vv'))
# print(re.split('\S', 'abc\r1dc\nb2vv'))
# print(re.findall('\s', 'abc\r1dc\nb2vv'))

print(re.split('\d', 'abc1dcb2vv', 1))  # 拆分1次
