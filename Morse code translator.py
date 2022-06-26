"""This is a program to translate morsecode."""
while 1 > 0:
    result = []
    character = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','S','Y','Z','1','2','3','4','5','6','7','8','9','0','?','!','.',',',';',':','+','-','/','=']
    morsecode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','..--..','-.-.--','--..--','-.-.-.','---...','.-.-.','-....-','-..-.','-...-']
    print("提示：请将您的摩斯代码用”/“隔离\nTip: Please segregate your morse code with\"/\"")
    moscode_input = input("请输入摩斯密码\nPlease enter your morse code：")
    moscode_input_split = moscode_input.split('/')
    for each in moscode_input_split:
        result.append(character[morsecode.index(each)])
    print('\n')
    print("".join(result))
    print('\n')
