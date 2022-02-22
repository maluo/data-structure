# check lesson 6 lint code 385 - 1:44:35

# List
list_1 = [12, 15.6, True, 'hello', ['a', 'b']]
list_2 = [1, 2, 3, 4]
list_3 = list('hello')
list_4 = []

# Create
list_5 = list_2 + list_3
list_6 = list_2 * 3
list_2.append("james")

# 3rd item since index starts from 0
list_2.insert(2, 'abc')

#
list_2.extend(list_3)

# Read list
# Close range in front, open range at the end, same as range function

# Update list
# Slice
list_2[1:3] = [20, 30, 40]
# Last index -2
# print(list_2[:-2])
# print(list_2[1:])

# Remove
# by default pop the last one.
list_2.pop(0)

# remove the first meet element which is equal to 4.
list_2.remove(4)

# **the right side is open bound
# del list_2[0:2]

# sort and reverse
# list_2.sort()
# list_2.reverse()
# list_2.sort(reverse=True)
print(list_2)

#
if(2 not in list_2):
    print("in")

# 列表生成器
result = []
for i in range(101):
    if i % 5 == 0:
        result.append(i)
print(result)

result1 = [i for i in range(101) if i % 5 == 0]
result2 = [0 for i in range(10)]
print(result2)