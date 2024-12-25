import sqlite3
import json

def export_clients_to_json(db_name, json_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Clients')
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    clients = []
    for row in rows:
        client_data = {columns[i]: row[i] for i in range(len(columns))}
        clients.append(client_data)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(clients, f, ensure_ascii=False, indent=4)

    print(f"Данные клиентов экспортированы в {json_file}.")
    conn.close()

def import_clients_from_json(db_name, json_file):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(json_file, 'r', encoding='utf-8') as f:
        clients = json.load(f)

    for client in clients:
        cursor.execute('''
            INSERT INTO Clients (client_id, name, email, phone)
            VALUES (?, ?, ?, ?)
        ''', (client['client_id'], client['name'], client['email'], client['phone']))

    conn.commit()
    print(f"Данные клиентов импортированы из {json_file}.")
    conn.close()
if __name__ == "__main__":
    export_clients_to_json('insurance_company.db', 'clients.json')
    import_clients_from_json('insurance_company.db', 'clients.json')