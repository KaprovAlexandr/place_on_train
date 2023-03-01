a = input("Введите ваш номер места: ")
if (int(a) % 2 == 0) and (int(a) >= 2 and int(a) <= 36):
    print("Купе, верхнее")
elif (int(a) % 2 != 0) and (int(a) >= 1 and int(a) <= 35):
    print("Купе, нижнее")
elif (int(a) % 2 == 0) and (int(a) >= 38 and int(a) <= 54):
    print("Боковое, верхнее")
elif (int(a) % 2 != 0) and (int(a) >= 37 and int(a) <= 53):
    print("Боковое, нижнее")
else:
    print("Такого места не существует!")

