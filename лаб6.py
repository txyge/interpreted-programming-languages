
def main():
    from collections import defaultdict

    filename = 'test6.txt'

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()

    N = int(data[0])  # Число элементов
    parent_dict = {}
    children_dict = defaultdict(list)

    # Считываем пары потомок-родитель
    for i in range(1, N):
        descendant, parent = data[i].split()
        parent_dict[descendant] = parent
        children_dict[parent].append(descendant)

    # Находим родоначальника (чей родитель не указан)
    all_descendants = set(parent_dict.keys())
    all_parents = set(parent_dict.values())
    root = list(all_parents - all_descendants)

    if root:
        root = root[0]  # Получаем родоначальника, если он найден
    else:
        print("Родоначальник не найден!")
        return

    # Словарь для хранения высот
    heights = {}

    # Функция для вычисления высоты
    def calculate_height(node, height):
        heights[node] = height
        for child in children_dict[node]:
            calculate_height(child, height + 1)

    # Начинаем с родоначальника
    calculate_height(root, 0)

    # Сортируем имена в лексикографическом порядке
    sorted_names = sorted(heights.keys())

    # Выводим имена и их высоты
    for name in sorted_names:
        print(f"{name} {heights[name]}")

if __name__ == "__main__":
    main()