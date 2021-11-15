# Author: JD 11/15/2021

li = input("Enter a list of words or numbers separated by spaces: ")

li = li.split()

end = len(li) - 1

deter = input("Do you want the ends of the middle? (middle/ends): ")

if deter == "ends":
    print(li[0], li[end])
elif deter == "middle":
    print(li[1 : end])
