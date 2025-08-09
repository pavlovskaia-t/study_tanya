import csv
with open ('random.csv',newline = '') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  #тут запоминаем хедер, что б перенести его в новый файл
    new_set = set()   #создаем сет для переноса новых данных.Именно сет, потому что там ТОЛЬКО уник. значения
    for stroka in reader:
        tuple_stroka = tuple(stroka)    #тут каждую строку делаем туплом
        if tuple_stroka not in new_set:
            new_set.add(tuple_stroka)
with open('result_pavlovskaya1.csv',"w",newline='') as new_cvs_file:
    writer = csv.writer(new_cvs_file)
    writer.writerow(header)
    writer.writerows(new_set)

with open ('rmc.csv',newline = '') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    new_set = set()
    for stroka in reader:
        tuple_stroka = tuple(stroka)
        if tuple_stroka not in new_set:
            new_set.add(tuple_stroka)
with open('result_pavlovskaya2.csv',"w",newline='') as new_cvs_file:
    writer = csv.writer(new_cvs_file)
    writer.writerow(header)
    writer.writerows(new_set)