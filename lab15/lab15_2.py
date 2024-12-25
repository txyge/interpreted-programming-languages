import csv
from datetime import datetime, timedelta
from charset_normalizer import detect

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = detect(raw_data)
        return result['encoding']

def parse_time_spent(time_str):
    try:
        days, hours, minutes, seconds = 0, 0, 0, 0

        if 'дн.' in time_str:
            parts = time_str.split('дн.')
            days = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'ч.' in time_str or 'час.' in time_str:
            parts = time_str.split('ч.') if 'ч.' in time_str else time_str.split('час.')
            hours = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'мин.' in time_str:
            parts = time_str.split('мин.')
            minutes = int(parts[0].strip())
            time_str = parts[1].strip() if len(parts) > 1 else ''

        if 'сек.' in time_str:
            parts = time_str.split('сек.')
            seconds = int(parts[0].strip())

        return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    except (IndexError, ValueError):
        raise ValueError(f"Некорректный формат времени: {time_str}")

def filter_test_results(file_path, max_time, exact_score):
    results = []

    encoding = detect_encoding(file_path)
    
    with open(file_path, 'r', encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Фамилия'].startswith('Среднее') or row['Имя'].startswith('Среднее'):
                continue

            if row['Состояние'] != 'Завершено':
                continue

            try:
                time_spent = parse_time_spent(row['Затраченное время'])
                score = float(row['Оценка/100,00'].replace(',', '.'))
            except ValueError as e:
                print(f"Ошибка при обработке строки: {e}. Исходные данные: {row}")
                continue

            if score == exact_score and time_spent <= max_time:
                results.append((row['Фамилия'], row['Имя'], time_spent))

    if results:
        results.sort(key=lambda x: x[2])
        min_time = results[0][2]
        min_time_participants = [name for name in results if name[2] == min_time]
        names = [name[0] + ' ' + name[1] for name in min_time_participants]
        names.sort()
        print("Количество участников с минимальным временем:", len(names))
        print("Список участников с минимальным временем в алфавитном порядке:")
        for participant in names:
            print(participant)
    else:
        print("Нет участников, соответствующих условиям.")

file_path = '12 - 2.csv'
max_time = timedelta(minutes=30)
exact_score = 90.0

filter_test_results(file_path, max_time, exact_score)
