import socket

# створюємо сокет_dev
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# задаємо IP-адресу та порт для серверу
server_address = ('127.0.0.1', 12345)
# прив'язуємо сервер до адреси та порту
server_socket.bind(server_address)
# очікуємо на вхідні підключення
server_socket.listen(1)
print("Сервер чекає на підключення...")
# приймаємо підключення
client_socket, client_address = server_socket.accept()
print(f"Підключено до {client_address}")

while True:
    # очікуємо та отримуємо дані від клієнта
    data = client_socket.recv(1024)
    if not data:
        break
    # виводимо отримані дані
    print(f"Клієнт: {data.decode('utf-8')}")
    # відправляємо відповідь клієнту
    message = input("Сервер: ")
    client_socket.send(message.encode('utf-8'))

# Закриваємо сокети
client_socket.close()
server_socket.close()
