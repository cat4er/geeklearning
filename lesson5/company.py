# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

with open('text_7.txt', 'r') as file:
    profitable = 0
    com_prof = 0
    profit_com = {}
    result = []
    for line in file:
        name, firm, earning, damage = line.split()
        profit_com[name] = int(earning) - int(damage)
        if profit_com.setdefault(name) >= 0:
            profitable = profitable + profit_com.setdefault(name)
            com_prof += 1
    if com_prof != 0:
        prof_aver = profitable / com_prof
    else:
        print(f'Все работают в убыток, сматываем удочки')
    result.append(profit_com)
    result.append({'Средняя прибыль': round(prof_aver)})

with open('task_7.json', 'w') as file_json:
    json.dump(result, file_json, ensure_ascii=False)
    js_str = json.dumps(result, ensure_ascii=False)
    print(f'\nСоздан файл с расширением json: \n \n \n'
          f' {js_str}')
