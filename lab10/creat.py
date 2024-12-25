import sqlite3

def create_database():
    # Подключение к базе данных (или создание ее, если она не существует)
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    # Создание таблицы Clients
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL
    )
    ''')

    # Создание таблицы Policies
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Policies (
        policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NOT NULL,
        policy_type TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (client_id) REFERENCES Clients(client_id)
    )
    ''')

    # Создание таблицы Claims
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Claims (
        claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_id INTEGER NOT NULL,
        claim_date DATE NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
    )
    ''')

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print("База данных и таблицы созданы успешно.")

    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

# Заполнение таблицы Clients
    clients_data = [
        ('Иван Иванов', 'ivan@example.com', '1234567890'),
        ('Петр Петров', 'petr@example.com', '0987654321'),
        ('Светлана Сидорова', 'svetlana@example.com', '1122334455'),
    ]
    cursor.executemany('INSERT INTO Clients (name, email, phone) VALUES (?, ?, ?)', clients_data)

    # Заполнение таблицы Policies
    policies_data = [
        (1, 'Автострахование', '2023-01-01', '2024-01-01'),
        (1, 'Страхование жизни', '2023-02-01', '2024-02-01'),
        (2, 'Страхование имущества', '2023-03-01', '2024-03-01'),
    ]
    cursor.executemany('INSERT INTO Policies (client_id, policy_type, start_date, end_date) VALUES (?, ?, ?, ?)', policies_data)

    # Заполнение таблицы Claims
    claims_data = [
        (1, '2023-05-01', 5000.00, 'Ожидает рассмотрения'),
        (2, '2023-06-01', 1500.00, 'Одобрено'),
        (3, '2023-07-01', 2500.00, 'Отклонено'),
    ]
    cursor.executemany('INSERT INTO Claims (policy_id, claim_date, amount, status) VALUES (?, ?, ?, ?)', claims_data)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print("База данных заполнена данными успешно.")

if __name__ == "__main__":
    create_database()