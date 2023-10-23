import socket

# створюємо сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# задаємо IP-адресу та порт сервера
server_address = ('127.0.0.1', 12345)
# підключення до сервера
client_socket.connect(server_address)

while True:
    # відправляємо повідомлення серверу
    message = input("Клієнт: ")
    client_socket.send(message.encode('utf-8'))
    # очікуємо на відповідь від сервера
    data = client_socket.recv(1024)
    # виводимо отриману відповідь
    print(f"Сервер: {data.decode('utf-8')}")

# закриваємо сокет
client_socket.close()
