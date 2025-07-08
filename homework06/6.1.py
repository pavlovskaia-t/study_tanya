#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# інакше - False.Строку отримати за допомогою функції input()

stroka = input("Введіть строку:")
stroka_set = set(stroka)
if len(stroka_set) > 10:
    print(True)
else:
    print(False)