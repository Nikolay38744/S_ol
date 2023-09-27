A = int(input("Ведите число чтобы угадать:"))
S = [0, 1, 2, 3]
if A in S:
    print("Bingo")
else:
    print(not A is S)