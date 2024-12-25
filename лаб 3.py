import re
from collections import Counter
import math

# В порядке увеличения разницы между средним количеством согласных и средним количеством гласных букв в строке.
def vowel_consonant_difference(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"  # Гласные буквы
    consonants = "бвгджзйклмнптфхцчшщБВГДЖЗЙКЛМНПТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  # Согласные буквы

    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)

    total_count = vowel_count + consonant_count
    if total_count == 0:
        return 0  # Если нет ни гласных, ни согласных, возвращаем 0

    average_vowels = vowel_count / total_count
    average_consonants = consonant_count / total_count

    return abs(average_consonants - average_vowels)

def sort_strings_by_difference(strings):
    return sorted(strings, key=vowel_consonant_difference)



# В порядке увеличения среднего количества "зеркальных" троек (например, "ada") символов в строке.
def clean_string(s):
    # Убираем все символы, кроме букв
    return re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', s)

def count_palindromic_triplets(s):
    count = 0
    length = len(s)

    for i in range(length - 2):
        triplet = s[i:i+3]  # Берем тройку символов
        if triplet == triplet[::-1]:  # Проверяем, является ли тройка палиндромом
            count += 1

    return count

def average_palindromic_triplets(s):
    if len(s) < 3:
        return 0  # Если строка меньше 3 символов, палиндромов нет
    return count_palindromic_triplets(s) / (len(s) - 2)

def sort_strings_by_average_palindromic_triplets(strings):
    return sorted(strings, key=lambda s: average_palindromic_triplets(clean_string(s)))


#В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого в строке символа
#от частоты его
#встречаемости в текстах на этом алфавите  
def sort_strings_by_deviation(strings):
    def calculate_deviation(s):
        # Очищаем строку от знаков препинания и приводим к нижнему регистру
        cleaned = re.sub(r'[^\w\s]', '', s.lower())
        # Считаем частоту символов
        freq = Counter(cleaned)
        # Находим самый частый символ
        most_common = freq.most_common(1)[0]
        # Вычисляем его частоту
        frequency = most_common[1] / len(cleaned)
        # Вычисляем квадратичное отклонение от эталонной частоты (11.5%)
        deviation = (frequency - 0.115) ** 2
        return deviation

    # Сортируем строки по возрастанию отклонения
    return sorted(strings, key=calculate_deviation)

#В порядке увеличения квадратичного отклонения между наибольши ASCII-кодом символа строки и разницы в ASCII-кодах пазеркально расположенных символов строки (относительно ее середины).
def calculate_deviation(s):
    # Получаем ASCII-коды символов
    ascii_codes = [ord(c) for c in s]
    
    # Находим максимальный ASCII-код
    max_ascii = max(ascii_codes)
    
    # Вычисляем разницы между зеркальными символами
    n = len(s)
    differences = []
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n-1-i]))
        differences.append(diff)
    
    # Вычисляем среднее значение разниц
    avg_diff = sum(differences) / len(differences) if differences else 0
    
    # Вычисляем квадратичное отклонение
    squared_deviations = [(max_ascii - diff)**2 for diff in differences]
    deviation = sum(squared_deviations) / len(squared_deviations) if squared_deviations else 0
    
    return deviation

strings = [ "Потерянный мир, где все было не так.",
    "Тот, кто не рискует, тот не пьет шампанское на свадьбе.",
    "А в лесу родилась ёлочка с красочными украшениями.",
    "Слон и Моська, которые стали лучшими друзьями.",
    "Madam, in Eden, I'm Adam, и я здесь один.",
    "Was it a car or a cat I saw in the garden?",
    "Step on no pets, и не забудь о них.",
    "A man, a plan, a canal: Panama, — вот моя мечта.",
    "Далеко-далеко за словесными горами, где живут чудеса.",
    "На свете много чудес, и все они в нашей голове, если только верить.",
    "Словно в сказке, да не в сказке, а в реальной жизни.",
    "Время — лучший учитель, но, к сожалению, оно убивает своих учеников, если не использовать его правильно.",
    "Каждый день — это новая жизнь, полная возможностей.",
    "На всякого мудреца довольно простоты, но мудрость — это сложно.",
    "Язык — это не просто средство общения, это ключ к пониманию и любви.",
    "Счастье — это не цель, а способ жизни, который каждый должен найти для себя."
]

print("\n")

sorted_strings1 = sort_strings_by_difference(strings)
for s in sorted_strings1:
    print(s)

print("\n ------------ \n")
sorted_strings2 = sort_strings_by_deviation(strings)

# Выводим отсортированные строки
for s in sorted_strings2:
    print(s)
    
print("\n ------------ \n")

# Сортируем строки
sorted_strings3 = sorted(strings, key=calculate_deviation)

# Выводим отсортированный список
for s in sorted_strings3:
    print(f"{s}\n\tОтклонение: {calculate_deviation(s):.2f}")
    
print("\n ------------ \n")
strings = [
    "ada",
    "abc",
    "racecar",
    "noon",
    "abba",
    "xyzzy",
    "a",
    "aaa"
]

sorted_strings3 = sort_strings_by_average_palindromic_triplets(strings)
for s in sorted_strings3:
    print(s)