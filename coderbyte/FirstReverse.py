# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
# For example: if the input string is "Hello World and Coders" then your program should return
# the string sredoC dna dlroW olleH.
#


def FirstReverse(str):
    s2 = []
    str1 = list(str)
    l = len(str1)
    # code goes here
    for i in range(l):
        s2.append(str[l - 1 - i])
    str = ''.join(s2)
    return str


# keep this function call here
result = FirstReverse("Hello World and Coders")
print(result)