# Complete the solution so that it reverses all of the words within the string passed in.
# reverseWords("The greatest victory is that which requires no battle")
# should return "battle no requires which that is victory greatest The"

import timeit

def reverseWords(str):
    r_str = []
    for word in str.split(" "):
        r_str.insert(0,word)   
    return " ".join(r_str)

def better_solution(str):
    return " ".join(str.split(" ")[::-1])

# a = reverseWords("Hello World!")
print ("My solution : ",timeit.timeit("reverseWords('Hello World!')","from __main__ import reverseWords",number=1000))
print ("Better solution : ",timeit.timeit("better_solution('Hello World!')","from __main__ import better_solution",number=1000))

# print(a)
