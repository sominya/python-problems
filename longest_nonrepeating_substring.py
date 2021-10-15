# Find the length of longest non - repeating substring in a string
# Example abcbacbdabcd,,, anwser is 4 acbd and abcd
def longsubstr(s):
    long_str=''
    prev=''
    length=[]
    for i in s:
        cur = i
        if cur in long_str:
            long_str=''
        else:
            long_str=long_str+cur
        length.append(len(long_str))
    return max(length)
