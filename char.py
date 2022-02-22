# python中不存在字符类型
# 普通字符&转义字符(\,esclation mark)
# 字符的储存
# 整数形式储存
## ord() & chr()

ch = 'a'
ch1 = 'A'
ch2 = '字'
print(ord('字'))  # order -> get unicode
print(chr(23383))

lower_char = 'q'
print(chr(ord(lower_char) - ord('a')+ord('A')))
print(lower_char.upper())