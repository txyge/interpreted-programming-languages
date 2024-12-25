import re

def is_valid_ipv4(ip):
   
    # Регулярное выражение для проверки IPv4 адреса
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def validate_ipv4(ip):
   
    if is_valid_ipv4(ip):
        return ip
    else:
        raise ValueError(f"Некорректный IP-адрес: {ip}")

# Примеры использования
try:
    ip_address = "192.168.1.1"
    print(f"{ip_address} является корректным IP-адресом: {is_valid_ipv4(ip_address)}")
    print(f"Валидированный IP-адрес: {validate_ipv4(ip_address)}")
    
    invalid_ip_address = "256.256.256.256"
    print(f"{invalid_ip_address} является корректным IP-адресом: {is_valid_ipv4(invalid_ip_address)}")
    print(f"Валидированный IP-адрес: {validate_ipv4(invalid_ip_address)}")
except ValueError as e:
    print(e)
