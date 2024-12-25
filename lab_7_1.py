import re

def find_common_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Разделяем текст на предложения
    sentences = re.split(r'[.!?]', text)

    # Создаем список множеств слов для каждого предложения
    word_sets = []
    for sentence in sentences:
        # Убираем лишние пробелы и знаки препинания, затем разбиваем на слова
        words = set(re.findall(r'\b\w+\b', sentence.lower()))  # Приводим к нижнему регистру
        if words:  # Добавляем только непустые множества
            word_sets.append(words)

    if not word_sets:
        print("Нет предложений в тексте.")
        return

    # Находим пересечение всех множеств
    common_words = set.intersection(*word_sets)

    if common_words:
        print("Слова, встречающиеся в каждом предложении:", ', '.join(common_words))
    else:
        print("Нет слова, которое встречается в каждом предложении.")

# Пример вызова функции
file_path = 'текст.txt'  # Укажите путь к вашему файлу
find_common_word(file_path)
