""" Напиши код с инструкцией elif """

print("Угадай число")
D = int(input(" Ведите число от 1 до 5:"))
B = input(" Веди букву:")
if D == 3:
    print("Угадал")
elif D == 0:
    print(" Не угодал ")
elif D > 3:
    print(" Близко ")
elif D < 3:
    print(" Горечо ")
else:
    print(B)
print("Конец")
