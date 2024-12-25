import sqlite3

def execute_queries():
    # Подключение к базе данных
    conn = sqlite3.connect('insurance_company.db')
    cursor = conn.cursor()

    # 1. Общее количество клиентов
    cursor.execute("SELECT COUNT(*) AS total_clients FROM Clients;")
    total_clients = cursor.fetchone()[0]
    print(f"Общее количество клиентов: {total_clients}")

    # 2. Общее количество полисов по типу
    cursor.execute("SELECT policy_type, COUNT(*) AS total_policies FROM Policies GROUP BY policy_type;")
    policies_count = cursor.fetchall()
    print("Общее количество полисов по типу:")
    for policy_type, total in policies_count:
        print(f"  {policy_type}: {total}")

    # 3. Общая сумма страховых выплат
    cursor.execute("SELECT SUM(amount) AS total_claims_amount FROM Claims;")
    total_claims_amount = cursor.fetchone()[0]
    print(f"Общая сумма страховых выплат: {total_claims_amount:.2f}")

    # Закрытие соединения
    conn.close()

if __name__ == "__main__":
    execute_queries()
