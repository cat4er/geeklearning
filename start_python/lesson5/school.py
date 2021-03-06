# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result = {}
with open('text_6.txt') as file:
    for line in file:
        text = line.split()
        key = ''
        value = []
        for word in text:
            w = ''
            n = ''
            for sym in word:
                if sym.isalpha():
                    w = w + sym
                if sym.isdigit():
                    n = n + sym
            if len(w) > 3:
                key = key + w
            if n:
                value.append(int(n))
        result.update({key: sum(value)})
print(result)
file.close()
