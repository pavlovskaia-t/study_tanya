#Реалізуйте ітератор для зворотного виведення елементів списку.
class FirstIterator:
    def __init__(self,lst):
        self.lst = lst
        self.index = len(lst)
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lst[self.index]

for el in FirstIterator([1,2,'hgjg',3,7]):
    print(el)
print("-"*80)
#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class SecondIterator:
    def __init__(self,n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return(self)
    def __next__(self):
        while self.current <= self.n:
            val = self.current
            self.current += 1
            if val % 2 == 0:
                return val
        raise StopIteration

for num in SecondIterator(15):
    print(num)