""" Напишите программу с Булевым оператором and """

print("Угадай число до 4")
A = int(input("Ведите число:"))
if (A == 1) and ( 1 == 1):
    print("Угадал1")
elif A != 2 and 2 == 2:
    print("Не угадал2")
elif A == 1 and 3 == 3:
    print("Не угадал3")
else:
    print("И опять не угадал")
print("Конец игры")