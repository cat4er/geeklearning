# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng2rus = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
file2 = open('task4.txt', 'w')
with open('text_4.txt') as file:
    for line in file:
        a = line.split()
        for key in eng2rus.keys():
            if a.count(key) == 1:
                ind = a.index(key)
                a.pop(ind)
                a.insert(ind, eng2rus.get(key))
        print(*a, file=file2)
file.close()
file2.close()

