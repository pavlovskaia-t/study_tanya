# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?" \n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '\"I don\'t much care where\" said Alice.\n'
                       '\"Then it doesn\'t matter which way you go,\" said the Cat.\n'
                       '\"So long as I get somewhere,\" Alice added as an explanation.\n'
                       '\"Oh, you\'re sure to do that,\" said the Cat, \"if you only walk long enough.\"')

print (alice_in_wonderland)
print()


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
s_black = 436402
s_azov = 37800
sum = s_azov + s_black
text = (f"Площа Чорного моря становить {s_black} км2, \n"
        f"а площа Азовського моря становить {s_azov} км2. \n"
        f"Додаємо: {s_black} + {s_azov} = {sum} \n"
        f"Відповідь: {sum} км2 - площа двох морів")
print(text)
print()

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
general = 375291
first_second = 250449
second_third = 222950
third = general - first_second
second = second_third - third
first = general - second - third
text2 = f'''Для початку дізнаємось кількість речей на третьому складі: {general} - {first_second} = {third}
Далі дізнаємось кількість речей на другому складі: {second_third} - {third} = {second}
І обчислюємо скільки речей на першому складі: {first_second} - {second} = {first}
Відповідь: на першому складі {first} товарів, на другому {second}, а на третьому {third}'''
print(text2)
print()



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
per_month = 1179
year = int(12)
months = int(year * 1.5)
total = int(per_month * months)
text = (f"{year} * 1,5  = {months} переводимо півтора року у  місяці \n"
        f"{per_month} * {months} = {total}- рахуємо загальну сумму \n"
        f"Відповідь:{total} грн ")
print(text)
print()

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a,b,c,d,e,f = 8019%8, 9907%9, 2789%5, 7248%6, 7128%5, 19224%9
print(f"a){a}     d){d} \n"
      f"b){b}     e){e} \n"
      f"c){c}     f){f}")
print()

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_p = 274
mid_p = 218
sok = 35
tort = 350
voda = 21
c_big_p = int(input("Кількість великих піц:"))
c_mid_p = int(input("Кількість середніх піц:"))
c_sok = int(input("Кількість соків:"))
c_tort = int(input("Кількість тортів:"))
c_voda = int(input("Кількість води:"))
result = big_p*c_big_p + mid_p*c_mid_p + sok*c_sok + tort*c_tort + voda*c_voda
print(f"Загальна сума: {result} грн")
print()

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total = 232
max = 8
result = int(total/max)
print(f"Ділимо кількість фотографій на кількість сторінок: {total} \ {max} = {result} сторінок")
print()


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
dist = 1600
fuel_per100 = 9
bak = 48
total_fuel = int(dist / 100 * fuel_per100)
refuel = int(total_fuel / 48)
print(f"Потрібно {total_fuel} літрів бензину, і {refuel} разів заїхати на заправку")