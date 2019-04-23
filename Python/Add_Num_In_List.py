#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

k = 17
n_list = [10,15,3,7]

for x in n_list:
    if (17 - x) in n_list:
        print (True) 
        break
