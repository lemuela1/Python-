"""文字转换器"""

x = input("请输入您的原文：")
y = input("请输入您需转换的文字：")
z = input("您想将其换成什么？：")
nums = x.count(y)
nums2 = x.count(y)
x_ = []
result = []
while nums > 0:
    x_.append(list(x.partition(y))[0])
    x_.append(list(x.partition(y))[1])
    x = list(x.partition(y))[2]
    nums -= 1
x_.append(x)
print(x_)
for each in x_:
    if each == y:
        result.append(z)
    else:
        result.append(each)


Print = ''.join(result)
print('\n')
print(Print)
print('\n')
