'''Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
інакше - False'''
def has_more_than_10_unique_chars(stroka):
    stroka_set = set(stroka)
    return len(stroka_set) > 10

'''Написати функцію, яка приймає список слів та повертає найдовше слово у списку.'''
def find_longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def asd(a:float, b:float):
    return (a+b)/2
