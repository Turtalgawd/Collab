import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1',12345))
my_socket.listen()

game_socket,addr = my_socket.accept()
print('Connected to client')

targets = []
board = []
y = -1
with open('GAME.txt','r') as f:
    for line in f:
        y += 1
        for x, char in enumerate(line):
            if char == 'S':
                targets.append((x,y))
f.close()
board = [['.']*12 for _ in range(8)]

for row in board:
    row = ''.join(row)
    