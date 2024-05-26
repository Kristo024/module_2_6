def single_root_words (list_):
    root_world = list_ [0] # в корень идёт первое слово
    list_.remove(root_world) #
    other_words = list_  # "... а далее неограниченную последовательность в параметр *other_words"
    root_world = root_world.lower()
    same_words = []
# разложение списка побуквенно
    for i in other_words:  # помещаем слова в  i   поочерёдно.
        n = 0
        n_max = 0  # обнуляем счётчики перед новым словом
        if i == "Mable":  # локальное исключение фамилии Mable из списка однокоренных к able
            continue
        for j in i:     # разбиваем слово побуквенно
            j = j.lower()  # переводим в строчные  буквы
# алгоритм стемминга
            if root_world.count(j) >= 1:   # если буква есть
                n += 1 # заносим в счётчик
                if n_max < n:  # чтобы дубль буквы корня отделённый от корня не уменьшал n_max
                    n_max = n  # длина совпадений
            else:
                n = 0
        if n_max >= 4:  # определение корня как 4-х подряд совпавших букв даже если не по порядку в корне
            same_words.append(i)  # добавляем слово в список однокоренных
        #print('same_words: ', same_words)
    return same_words

# задание неограниченной последовательности в виде списка
a1 = ['rich', 'richiest', 'orichalcum', 'cheers', 'richies']
a2 = ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel']

result1 = single_root_words(a1)
result2 = single_root_words(a2)
print(result1)
print(result2)