import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1',12345))
my_socket.listen()
print('Waiting connection.....')

targets = []
y = -1
with open('GAME.txt','r') as f:
    for line in f:
        y += 1
        for x, char in enumerate(line):
            if char == 'S':
                targets.append((x,y))
f.close()
board = [['.']*12 for _ in range(8)]

array = ''
for row in board:
    row = ' '.join(row)
    array += row + '\n'

game_socket,addr = my_socket.accept()
print('Connected to client')

hits = []
attempts = 7
for i in range(7):
    if i == 0:
        game_socket.send(b'Game start\n' + array.encode())
    print('Waiting for coords...')

    rec = game_socket.recv(1024).decode()
    print(rec)
    status = ''
    xcoord, ycoord = rec.split(',')
    xcoord = int(xcoord)
    ycoord = int(ycoord)
    shoot = (xcoord,ycoord)
    if shoot in targets:
        hits.append(shoot)
        board[ycoord][xcoord] = 'X'
        status = 'Hit'
        print(status)
    else:
        board[ycoord][xcoord] = 'O'
        status = 'Miss'
        print(status)
    
    array = ''
    for row in board:
        row = ' '.join(row)
        array += row + '\n'
    
    game_socket.send(array.encode() + status.encode())

y=-1
with open('GAME.txt','r') as f:
    for line in f:
        y += 1
        for x, char in enumerate(line):
            if char == 'S':
                if board[y][x] == '.':
                    board[y][x] = 'S'
f.close()
array = ''
for row in board:
    row = ' '.join(row)
    array += row + '\n'
game_socket.send(array.encode() + b'Game over\n')

my_socket.close()
game_socket.close()