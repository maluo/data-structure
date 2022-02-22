# 数据不可变，但是较为安全，哪怕传参数之后也不可修改
# tuple可以做hash，list不可以
# tuple操作会比list快
# lesson6 - 2:31:11 explain difference on value vs reference
# 赋值操作和函数传参都是在赋值地址

tuple_1 = (12,15.6,True,'hello',['a','b'])
tuple_2 = (1,2,3,4)
tuple_3 = tuple('hello')
tuple_4 = 20

# Read
for x in tuple_2:
    print(x, end=' ')

print(tuple_2[0])
print(tuple_2[3])
      
# 
print(id(tuple_2))