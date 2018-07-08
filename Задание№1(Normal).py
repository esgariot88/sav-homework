# Задача №1

while True:
    Number = int(input("Ввведите число:"))

    if Number < 10 and Number > 0:
         print("Условия выполнены")
         print(Number ** 2)
         break

    else:
         print("Условия не выполнены.Введите число больше 0,но меньше 10.")


# Задача №2

Number_1 = 10
Number_2 = 20

Number_1 = int(input("Введите исходное значение N_1:"))
Number_2 = int(input("Введите исходное значение N_2:"))

if Number_1 ==10:
   Number_1=20
   print("N_1=" + str(Number_1))


else:
    print("Введите исходное значение")

if Number_2 ==20:
   Number_2=10
   print("N_2=" + str(Number_2))
else:
        print("Введите сходное значение")
