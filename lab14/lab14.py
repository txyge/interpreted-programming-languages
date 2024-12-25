import xml.etree.ElementTree as ET
from collections import defaultdict

# Загружаем XML-данные
# Здесь укажите путь к вашему файлу с данными OSM
file_path = "12 -2.osm"

# Парсим XML-файл
tree = ET.parse(file_path)
root = tree.getroot()

# Словарь для группировки ресторанов по времени работы
restaurants_by_time = defaultdict(list)

# Префикс пространства имен OSM
ns = {"osm": "http://www.openstreetmap.org"}

# Проходим по всем узлам (node) в XML
for node in root.findall("node"):
    tags = {tag.attrib["k"]: tag.attrib["v"] for tag in node.findall("tag")}
    
    # Проверяем, является ли объект рестораном
    if tags.get("amenity") == "restaurant":
        name = tags.get("name", "Неизвестное название")
        opening_hours = tags.get("opening_hours")
        
        if opening_hours:
            # Извлекаем время начала работы
            try:
                start_time = opening_hours.split(";")[0].split("-")[0].strip()
                restaurants_by_time[start_time].append(name)
            except Exception as e:
                print(f"Не удалось обработать время работы для {name}: {e}")

# Вывод результатов
for start_time, restaurants in sorted(restaurants_by_time.items()):
    print(f"Рестораны, открывающиеся с {start_time}:")
    for restaurant in restaurants:
        print(f"  - {restaurant}")
