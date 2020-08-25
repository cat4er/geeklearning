# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import deque

companies = deque()  # было бы промышленное решеие то очередь вполне бы пригодилась.
structure = ('company', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'year_profit')
Quarters = 4
profit_sum = 0

company_count = int(input('Введите количество предприятий: '))
count = 0

while count != company_count:
    count += 1
    _year_profit = 0
    _name = input(f'Введите название {count}-го предприятия: ')
    _dict = {}
    _dict.update({'company': _name})
    for i in range(1, Quarters + 1):  # завязался на кол-во кварталов, но можно на длину структуры.
        _quarter_profit = float(input(f'Введите прибыль {_name} в {i} квартале: '))
        _dict.update({structure[i]: _quarter_profit})
        _year_profit += _quarter_profit
        profit_sum += _quarter_profit
        _dict.update({'year_profit': _year_profit})
    companies.append(_dict)

if company_count == 1:
    print(f'Сравнивать "{companies[0]["company"]}" не с кем. Eго годовая прибыль: {companies[0]["year_profit"]}')

else:
    profit_average = profit_sum / company_count

    less_average = []
    more_average = []

    for i in range(company_count):
        if companies[i]["year_profit"] < profit_average:
            less_average.append(companies[i]["company"])
        elif companies[i]["year_profit"] > profit_average:
            more_average.append(companies[i]["company"])

    print(f'Средняя годовая прибыль предприятий составила: {profit_average: .2f}')
    print(f'Предприятия, чья прибыль меньше средней: {", ".join(less_average)}')
    print(f'Предприятия, чья прибыль больше средней: {", ".join(more_average)}')


