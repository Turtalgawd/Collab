import socket
player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = input('Enter IPv4 address: ')
port = int(input('ENter port number: '))

player.connect((address,port))
while True:
    data = player.recv(1024).decode()
    print(data)
    if 'START' in data:
        length = data[6:].strip()
        current_word = '?'*int(length)
    elif 'WIN' in data or 'LOSE' in data:
        if 'WIN' in data:
            print('You win!')
            break
        else:
            print('You lose!')
            break
    elif 'GUESS' in data:
        for char in data:
            if char.isnumeric():
                current_word = list(current_word)
                current_word[int(char)] = letter
                current_word= ''.join(current_word)
    print(f'Current word: {current_word}')
    response = ''
    while response not in ['GUESS','HWORD','QUIT']:
        response = input('Pick an action (GUESS/HWORD/QUIT): ').upper()
    match response:
        case 'GUESS':
            letter = ''
            while not letter.isalpha() or len(letter) != 1:
                letter = input('Guess a letter: ').lower()
            msg = f'{response},{letter}'
            msg += '\n'
            player.send(msg.encode())
        case 'HWORD':
            word = ''
            while not word.isalpha() or len(word) != len(current_word):
                word = input('Guess word: ')
            msg = f'{response},{word}'
            msg += '\n'
            player.send(msg.encode())
        case 'QUIT':
            msg = f'{response}\n'
            player.send(msg.encode())
            break


player.close()