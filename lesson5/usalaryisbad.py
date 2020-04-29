# Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


with open('task3.txt') as file:
    salarybook = {}
    for line in file:
        a = line.split()
        salarybook.update({a[0]: float(a[1])})
loosers = []
for item in salarybook:
    if salarybook.get(item) < 20000:
        loosers.append(item)
print('Этим людям неплохо было бы поднять ЗП:', end=' ')
print(*loosers, sep=', ')
print(f'В целом, средняя ЗП по компании - {sum(salarybook.values()) / len(salarybook):.2f}')
file.close()
