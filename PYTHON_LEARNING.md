---
attachments: [Clipboard_2022-06-26-12-48-17.png, Clipboard_2022-06-26-13-22-27.png, Clipboard_2022-06-26-13-46-38.png, Clipboard_2022-06-26-13-46-44.png]
tags: [Python-learning]
title: PYTHON_LEARNING
created: '2022-06-26T07:54:47.937Z'
modified: '2022-06-26T18:49:45.217Z'
---

# PYTHON_LEARNING
This is a repository that I create for Python learning.

# Variable
An element, feature, or factor that is liable to vary or change.
Using assigment operator, you can assign something to Variable.
For example:

    >>> x = 2
    >>> x = [1,2,3]
    >>> x = (1,2,3)
    >>> x = "Lemuela"
    >>> x = "中文字符"

The value of variable equal to the last value you given.

    >>> x = 1
    >>> y = 3
    >>> x = y
    >>> x
    3

Variable can be characters, chinese, number and _. But variable can't start with number.

    >>> 2lemuela = 1
      File "<stdin>", line 1
        2lemuela = 1
        ^
    SyntaxError: invalid decimal literal

# String
A string is a data type used in programming, such as an integer and floating point unit, but is used to represent text rather than numbers.

    >>> x = "我是老乌龟“
    >>> x
    我是老乌龟
    >>> x =  "I'm Mr.turtle"
    >>> x
    I'm Mr.turtle

You can use three different ways to write String. They're 'single quotes'，" double quotes" and """'''triple quotes'''""".

    >>> x = 'apple'
    >>> x = "apple"
    >>> x = """apple"""
    >>> x = '''apple'''
    >>> x
    'apple'

And this can avoid some special situation.

    >>> x = 'let's go'
      File "<stdin>", line 1
        x = 'let's go'
                ^
    SyntaxError: invalid syntax
    >>> x = "let's go"
    >>> x 
    "let's go"

# Escape Character
An escape character is a character that invokes an alternative interpretation on the following characters in a character sequence.

    >>> x = 'let\'s go '
    >>> x
    "let's go"

Here is a list of way to utilize escape character.(chinese)
![](@attachment/Clipboard_2022-06-24-14-36-29.png)
# Raw String
Raw strings are raw string literals that treat backslash (\ ) as a literal character.

    >>> x = "D:\lemuela\apple\turtle"
    >>> x
    'D:\\lemuela\x07pple\turtle'
    >>> x = r"D:\lemuela\apple\turtle"
    >>> x
    'D:\lemuela\apple\turtle'

# Operation
## 1, Concatenation of strings
Int and string are not the same things, therefore:

    >>> bool( 520 == '520' )
    False

It's totally different when you operate addition toward int and string.

    >>> 520 + 1314
    1834
    >>> '520' + '1314'
    '5201314'

## 2, Multiplication of strings
Multipling strings means make more character of it rather than change it's value.

    >>> 520 * 3
    1560
    >>> '520' * 3
    '520520520'

## 3,operation of int
![](@attachment/Clipboard_2022-06-26-12-48-17.png)

    >>> 1 + 1
    2
    >>> 1 - 1
    0
    >>> 1 * 1
    1
    >>> 1 / 1
    1.0
    >>> 2 // 3
    0
    >>> 5 % 2
    1
    >>> -1
    -1
    >>> +1
    1
    >>> abs(-1)
    1
    >>> int('1')
    1
    >>> float('1')
    1.0
    >>> complex(1,3)
    (1+3j)
    >>> z = 1 + 1j
    >>> z.conjugate()
    (1-1j)
    >>> divmod(-3, 2)
    (-2, 1)
    >>> divmod(3, 2)
    (1, 1)
    >>> pow(2,3)
    8
    >>> 2 ** 3
    8

## operator precedence
![](@attachment/Clipboard_2022-06-26-13-22-27.png)

## Short-circuit evaluation
Python obey Short-circuit evaluation: Short-circuiting is a programming concept by which the compiler skips the execution or evaluation of some sub-expressions in a logical expression.

    >>> (not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
    4

# Compare Operators
Operators that compare values and return true or false.

    >>> bool( 1 == 1 )
    True
    >>> bool( 1 > 1 )
    False
    >>> bool( 1 < 1 )
    False

And here is a list of Compare Operators
![](@attachment/Clipboard_2022-06-24-15-32-25.png)

# Summary of Basic Functions
## 1, print()
  output the value inside your variable.

    >>> x = 2
    >>> print(x)
    2

## 2, input()
  Put (data) into your computer.

    >>> x = input('Your username:')
    Your username:lemuela
    >>> x
    'lemuela'
  
## 3, int()
  Transfer the value of a variable into a int.(only access number)

    >>> x = '520'
    >>> x
    '520'
    >>> int(x)
    520
    >>> bool( x == int(x))
    False

## 4, bool()
  Returns the boolean value(true or false) of a specified object.

    >>> bool( "I'm a girl" == "lemuela" )
    False
## 5, len()
  Get the number of character of a string have.(including space and other symbols)

    >>> x = "I love you"
    >>> len(x)
    10

## 6, About texture （ONLY FOR STRING)
### 1* capitalize()
  Converts the first character of a string to an uppercase letter and all other alphabets to lowercase.

    >>> x = "i love you"
    >>> x.capitalize()
    'I love you'

### 2* casefold()
  Returns a string where all the characters are lower case.

    >>> x = "I LOVE YOU"
    >>> x.casefold()
    'i love you'

### 3* title()
  Returns a string where the first character in every word is upper case.

    >>> x = "I'm the title"
    >>> x.title()
    "I'M The Title"

### 4* swapcase()
  Swap the uppercase into lowercase, lowercase to uppercase.

    >>> z = "I can swapcase"
    >>> z.swapcase()
    'i CAN SWAPCASE'

### 5* upper()
  Returns a string where all the characters are upper case.

    >>> c = "abcd"
    >>> c.upper()
    'ABCD'

### 6* lower()
  Returns a string where all the characters are lower case.

    >>> d = "ABCD"
    >>> d.lower()
    'abcd'

### 7* center(width, fillchar='')
  Center align the string, using a specified character (space is default) as the fill character.

    >>> x = "Wo Shi Ni BABA"
    >>> x.center(3)
    'Wo Shi Ni BABA'
    >>> x.center(30)
    '        Wo Shi Ni BABA        '
    >>> x.center(30,'baba')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: The fill character must be exactly one character long
    >>> x.center(30,'$')
    '$$$$$$$$Wo Shi Ni BABA$$$$$$$$'

### 8* ljust(width,fillchar='')
  adjust the string to the left and fill up the left of the string with width(number-len(x)) of ''.

    >>> x = "Wo Shi Ni BABA"
    >>> x.ljust(3)
    'Wo Shi Ni BABA'
    >>> x.ljust(30)
    'Wo Shi Ni BABA                '
    >>> x.ljust(30,'$')
    'Wo Shi Ni BABA$$$$$$$$$$$$$$$$'

### 9* rjust(width,fillchar='')
  Adjust the string to the right and fill up the right of the string with width(number-len(x)) of ''.

    >>> x
    'Wo Shi Ni BABA'
    >>> x.rjust(30,'$')
    '$$$$$$$$$$$$$$$$Wo Shi Ni BABA'

### 10* zfill('number-len(x)')
  Fill up the left of the string with 'number-len(x)' of 0.

    >>> x = "30.45"
    >>> y = "1.16"
    >>> x.zfill(5)
    '30.45'
    >>> y.zfill(6)
    '001.16'
    >>> x.zfill(6)
    '030.45'

# Conditional Branch
## 1, if-else:
The if-else statement is used to execute both the true part and the false part of a given condition. If the condition is true, the if block code is executed and if the condition is false, the else block code is executed.

    >>> x = 2
    >>> if x > 1:
    ...     print("x > 1")
    ...     x -= 1
    ... else:
    ...     print("x <= 1")
    ...
    x > 1
    >>> x = 0
    >>> if x > 1:
    ...     print("x > 1")
    ...     x -= 1
    ... else:
    ...     print("x <= 1")
    ...
    x <= 1

# Loops
## 1, For loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 

    >>> x = ['abc','ABC',1,2,3,4]
    >>> for each in x:
    ...  print(each)
    ...
    abc
    ABC
    1
    2
    3
    4
And this also work with strings.
    >>> x = 'lemuela'
    >>> for each in x:
    ...  print(each)
    ...
    l
    e
    m
    u
    e
    l
    a

## While loops
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. We generally use this loop when we don't know the number of times to iterate beforehand.

    >>> x = 10
    >>> while x > 1:
    ...     print(x)
    ...
    10
    10
    10
    10
    10
    ......

## Get out of the loop.
### Break:
'Break' in Python is a loop control statement. It is used to control the sequence of the loop. Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that. 

    >>> x = 10
    >>> while x > 1:
    ...  print(x)
    ...  break
    ...
    10

### continue:
The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

    >>> x = 10
    >>> while x > 1:
    ...  print(x)
    ...  continue
    ...  print(x*2)
    ...
    10
    10
    10
    10
    10
    ......

![](@attachment/Clipboard_2022-06-26-13-46-44.png)
