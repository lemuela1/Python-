"""This is a program to Decompress"""

x = input("请输入压缩字符串：\nPlease enter the strings that you trying to decompress:")
x1 = []
[x1.append(each) for each in x]

ch = 0
X_list = []
while len(x) > ch:
    if x1[ch].isdecimal():
        print(x1[ch])
        X_list.append(x[ch-1]*int(x1[ch]))
    ch += 1

result = ''.join(X_list)
print('\n')
print(result)
print('\n')
