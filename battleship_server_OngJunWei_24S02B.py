import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1',12345))
my_socket.listen()
print('Waiting connection.....')

targets = []
final = []
shots = 7
y = -1
with open('GAME.txt','r') as f:
    for line in f:
        y += 1
        line1 = list(line)
        final.append(line1)
        for x, char in enumerate(line):
            if char == 'S':
                targets.append((x,y))
f.close()
board = [['.']*12 for _ in range(8)]

game_socket,addr = my_socket.accept()
print('Connected to client')

while True:
    array = ''
    for row in board:
        row = ' '.join(row)
        array += row + '\n'
    array_final = ''
    for row in final:
        row = ' '.join(row)
        array_final += row 

    if shots == 7:
        game_socket.send(b'Game start\n' + array.encode())
    elif shots == 0:
        game_socket.send(array_final.encode() + b'Game over\n')
        break
    else:
        game_socket.send(array.encode())
    
    print('Waiting for coords...')
    xcoord, ycoord = game_socket.recv(1024).decode().split(',')
    xcoord = int(xcoord)
    ycoord = int(ycoord)
    loc = (xcoord,ycoord)
    if loc in targets:
        board[ycoord][xcoord] = 'X'
        final[ycoord][xcoord] = 'X'
        print(loc)
        print('Hit')
    else:
        board[ycoord][xcoord] = 'O'
        final[ycoord][xcoord] = 'O'
        print(loc)
        print('Miss')
    shots -= 1
my_socket.close()
game_socket.close()