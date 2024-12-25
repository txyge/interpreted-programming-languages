import sqlite3


print("Content-type: text/html\n")

conn = sqlite3.connect('insurance_company.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Clients')
rows = cursor.fetchall()

print("<h3>Клиенты</h3>")
print("<table border='1'><tr><th>ID</th><th>Имя</th><th>Email</th><th>Телефон</th></tr>")
for row in rows:
    print(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>")
print("</table>")



conn.close()