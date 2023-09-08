""" Написать программу контроля возраста """

A = int(input("Ведите свой возраст:"))
B = input("Ведите своё имя:")
if A >= 18:
    print("Welcome" + B)
else:
    print("Sorry", B)