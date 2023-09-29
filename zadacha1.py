def count_occurrences(list_1, k):
    count = 0  # Инициализируем счетчик

    for element in list_1:
        if element == k:
            count += 1

    return count

# Пример использования
list_1 = [1, 2, 2, 3, 4, 2, 5, 6, 2]
k = 2
occurrences = count_occurrences(list_1, k)
print(f"Число {k} встречается в массиве {occurrences} раз(а).")