from http.server import CGIHTTPRequestHandler, HTTPServer

# Создание CGI-сервера
PORT = 8000

server = HTTPServer(('localhost', PORT), CGIHTTPRequestHandler)
print(f"Сервер запущен на порту {PORT}.")
server.serve_forever()