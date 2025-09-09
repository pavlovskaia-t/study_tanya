#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def generator_first(n):
    for i in range (0,n):
        if i%2 ==0:
            yield i
gen = generator_first(18)
for num in gen:
    print(num)
print()
#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def generator_second(n):
    first = 0
    second = 1
    while first <n:
        yield first
        first,second = second, first+second
gen = generator_second(9)
for num in gen:
    print(num)