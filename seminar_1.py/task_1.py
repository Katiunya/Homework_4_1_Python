# вводится два числа, определить большее
a = int(input("Введите число а - "))
b = int(input("Введите число b - "))

if a < b:
    print(f"b = {b} больше a")
elif a > b:
    print(f"a = {a} больше b")   
else:
    print("a = b")   