import socket

json_mas = [[b"""{"menu": {"id": "file",
                           "value": "File",
                           "popup": {"menuitem": [{"value": "New", "onclick": "CreateNewDoc()"},
                                                  {"value": "Open", "onclick": "OpenDoc()"},
                                                  {"value": "Close", "onclick": "CloseDoc()"}
                                                  ]
                                     }
                           }
                }""", b'True'],
            [b"""{"widget": {"debug": "on",
                             "window": {"title": "Sample Konfabulator Widget",
                             "name": "main_window",
                             "width": 500,
                             "height": 500
                             },
                  "image": {"src": "Images/Sun.png",
                            "name": "sun1",
                            "hOffset": 250,
                            "vOffset": 250,
                            "alignment": "center"
                            },
                  "text": {"data": "Click Here",
                           "size": 36,
                           "style": "bold",
                           "name": "text1",
                           "hOffset": 250,
                           "vOffset": 100,
                           "alignment": "center",
                           "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
                           }
                  }
            }""", b'True'],
            [b"""Not a json""", b'False'],
            [{1: "one", 2: "two"}, b'False']]

HOST = "127.0.0.1"
PORT = 65432

# создаю сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    res = input('Send your data(1) or my data(0): ')
    if res == '1':
        send_json = input('Input your json:')
        s.sendall(bytes(send_json, 'utf-8'))
        data = s.recv(1024)
        print(f"Your json is real json? Answer: {data}")
    else:
        # Проверяю в цикле, что все результаты соответствуют ожидаемым
        for json, ans in json_mas:
            s.sendall(bytes(json))
            data = s.recv(1024)
            assert data == ans, f"{json} \nMy json valid is broken, my ans is {ans}, real ans is {str(data)}"
            print(f'{json} is real json? Answer: {data}', '\n')
        print("All tests are success")
    # отправляю close чтобы закрыть соединение
    s.sendall(b"close")
    data = s.recv(1024)
    print(data)
