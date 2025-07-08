#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numbers = input("Введіть список чисел без пробілів,ком,крапок і всього іншого:")
total = 0
numbers = list(numbers)
numbers_int = [int(x) for x in numbers]
for i in numbers_int:
    if i%2 == 0:
        total += i
print(total)