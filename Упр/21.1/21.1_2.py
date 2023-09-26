""" Напиши программу, при воде числа в которую выдаст название фрукта."""

fruits = ["Apple", "Cherry", "Banana"]
A = int(input())
if A < 0 or A > 2:
    print("Не угадал")
elif A > 0 or A < 2:
    print(fruits[A])
