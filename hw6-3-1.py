# Author: JD 11/15/2021

w1 = input("The first word: ")

w2 = input("The second word: ")

wd1 = list(w1)
wd1.sort()

wd2 = list(w2)
wd2.sort()

if wd1 == wd2:
    print(w1, "and", w2, "are anagrams.")
else:
    print(w1, "and", w2, "are not anagrams.")