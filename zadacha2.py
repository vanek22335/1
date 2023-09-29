def find_closest_element(list_1, k):
    closest_element = None  # Инициализируем переменные для хранения ближайшего элемента и разницы
    min_difference = float('inf')

    for element in list_1:
        difference = abs(element - k)  # Вычисляем разницу между текущим элементом и k
        if difference < min_difference:
            min_difference = difference
            closest_element = element

    return closest_element

# Пример использования
list_1 = [1, 2, 3, 4, 5]
k = 6
closest = find_closest_element(list_1, k)
print(f"Ближайший элемент к {k} в массиве: {closest}")