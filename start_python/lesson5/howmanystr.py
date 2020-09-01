# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open('task2.txt') as file:
    string = 0
    words = []
    for line in file:
        string += 1
        for _ in line.split():
            words.append(_)
print(f'количество строк в файле: {string}')
print(f'количество слов в файле: {len(words)}')
file.close()
