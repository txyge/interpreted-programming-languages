def find_max_sum_segment(file_path):
    with open(file_path, 'r') as f:
        # Считываем первую строку
        first_line = f.readline().strip()
        N, K = map(int, first_line.split())
        K+=1

        # Считываем высоты
        heights = [int(f.readline().strip()) for _ in range(N)]

    # Инициализация переменных для скользящего окна
    current_sum = sum(heights[:K])  # Сумма первых K элементов
    max_sum = current_sum  # Начальное значение для максимальной суммы

    # Перемещение окна по массиву
    for i in range(K, N):
        current_sum += heights[i] - heights[i - K]  # Добавляем следующий элемент и убираем первый элемент окна
        max_sum = max(max_sum, current_sum)

    return max_sum

# Пример вызова функции
file_test_7 = 'test.txt'
file_path_a = '27-170a.txt'
file_path_b = '27-170b.txt'

max_sum_test = find_max_sum_segment(file_test_7)
print("Максимальная оценка для файла test:", max_sum_test) # 550

max_sum_a = find_max_sum_segment(file_path_a)
print("Максимальная оценка для файла A:", max_sum_a) # 1254156

max_sum_b = find_max_sum_segment(file_path_b)
print("Максимальная оценка для файла B:", max_sum_b) # 45076190
