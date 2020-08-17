# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9.


MIN_ITEM = 2
MAX_ITEM = 99
MIN_MULTIPLE = 2
MAX_MULTIPLE = 9

array = [a for a in range(MIN_ITEM, MAX_ITEM + 1)]
for e in range(MIN_MULTIPLE, MAX_MULTIPLE + 1):
    exec('multiple_%s = 0 ' % e)
    for i in array:
        if i % e == 0:
            exec('multiple_%s += 1 ' % e)
    print(f'Из диапозона от {MIN_ITEM} до {MAX_ITEM} числу {e} кратны {globals()["multiple_%s" % e]} числа(ел)')