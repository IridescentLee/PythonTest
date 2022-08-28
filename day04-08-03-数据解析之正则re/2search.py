import re
# 匹配一位小写字母
# search 匹配一次  字符串中包含就可以
# print(re.search('[a-z]', '123456a'))
# print(re.search('[a-z]{2}', '123456a'))
# print(re.search('[a-z]{2}', '123456ab'))
# print(re.search('[a-z]{2}', '123456abc'))
# print(re.search('[a-z]{2,}', '123456abasdasd'))
# print(re.search('[A-Z]{2,}', '12ABC3456abasdasd'))
# print(re.search('[A-Za-z]{2,}', '12ABC3456abasdasd'))
# print(re.search('[A-Za-z]{4,}', '12ABC3456abasdasd'))
# print(re.search('[A-Za-z0-9]', '12ABC3456abasdasd'))

# print(re.search('1[3-9][0-9]{9}', '12345678901'))
# print(re.search('1[3-9][0-9]{9}', '13345678901'))

# 包含 并不是完全匹配
# print(re.search('^1[3-9][0-9]{9}$', '13345678901123'))
# print(re.search('^1[3-9][0-9]{9}$', '13345678901'))

# print(re.search('^[0-9]', '1a'))
# print(re.search('^[0-9]', 'a1a'))
print(re.search('[^0-9]', '1a'))  # 匹配一位非数字就可以
