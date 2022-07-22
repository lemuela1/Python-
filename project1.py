def fuc1(Obj, Sub):
    sub = 0
    ob = 0
    while sub < len(Sub):
        if Obj[ob] == Sub[sub]:
            sub += 1
            ob += 1
        elif Obj[ob] != Sub[sub]:
            ob += 1
        elif ob == len(Obj) + 1:
            break
    if sub == len(Sub):
        p: str = f"{Sub}是{Obj}的子序列"
        print(p)
    else:
        print(f"{Sub}不是{Obj}的子序列")


s = input('请输入字符串1：')
t = input('请输入字符串2：')

if len(s) > len(t):
    Sub_ = t
    Ob_ = s
if len(t) > len(s):
    Ob_ = t
    Sub_ = s
fuc1(Ob_, Sub_)