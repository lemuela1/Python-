"""This is a program to compress a strings"""

String_input = input("请输入字符串\nPlease enter your strings:")
ch = 0
result = []
numbers = 1
while ch <= len(String_input):
    if len(String_input) == ch+1:
        if numbers == 1:
            result.append(String_input[ch])
            break
        else:
            result.append(String_input[ch])
            result.append(str(numbers))
            break
    if String_input[ch] == String_input[ch+1]:
        numbers += 1
    else:
        if numbers <= 2:
            result.append(String_input[ch])
            ch += 1
            continue
        else:
            result.append(String_input[ch])
            result.append(str(numbers))
            numbers = 1
    ch += 1

x = ''.join(result)
print(x)

rate = len(x)/len(String_input)
print('压缩率为：', rate, '\n', 'Compressing rate is:', rate)
