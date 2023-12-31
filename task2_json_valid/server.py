import socket
import json


def is_json(my_json):
    try:
        # Проверяю на возможность перевести из json
        print(my_json)
        my_json = json.loads(my_json.decode("utf-8"))
        if type(my_json) == 'dict':
            return b'False'
        return b'True'
    except ValueError as e:
        return b'False'


print('start server')

HOST = "127.0.0.1"
PORT = 65432

# Запускаю сервер до передачи b'close'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            # проверяю что сообщение не пустое и не close
            if data != b'close':
                # Отправляю результат работы функции на переданных данных
                conn.sendall(is_json(data))
            else:
                conn.sendall(b'close connection')
                break
print("close connection")
