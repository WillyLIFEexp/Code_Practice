# Challenge from Daily Coding
# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


import string

chars = string.ascii_lowercase
num_case = dict()

for num,char in enumerate(chars):
    num_case[char] = str(num+1)

print(num_case)

input_num = input("Please enter three number :")

if '0' in input_num:
    print ("False input")
else:
    print ("True input")

tmp_num = 0
for num in input_num:
    tmp_num += int(num)


