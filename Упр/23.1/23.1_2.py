""" Напиши программу с использованием функции len """

print("Угадай длину от 1 до 10")
A = int(input("Веди число:"))
nu = [1, 2, 3, 4]
if A < 0 or A > len(nu):
    print("Не угадал")
else:
    print(nu)
    print(len(nu))