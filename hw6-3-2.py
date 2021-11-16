# Author: JD 11/15/2021

num = input("give me a list of numbers: ")

li = num.split()

li2 = li.copy()

li2.sort()

if li == li2:
    print("the list is sorted")
else:
    print("the list is not sorted")
