import socket, threading

import game

player1 = game.Player(1, socket, 0)
player2 = game.Player(2, socket, 0)


def handle_player(conn, addr):
    global player1
    global player2
    try:
        if player1.symbol == "X":
            print('mam 2')
            player2 = game.Player('O', conn, addr)
    except NameError:
        print('mam 1')
        player1 = game.Player('X', conn, addr)


def connect_to_server(s):
    s.listen()
    conn, addr = s.accept()
    global player1
    global player2
    if player1.symbol == "X":
            print('mam 2')
            player2 = game.Player('O', conn, addr)
    else:
        print('mam 1')
        player1 = game.Player('X', conn, addr)


def turn_of_game(player, battlefield):
    print('jsem tu')
    player.socket.send((battlefield.display() + f"\nyour move").encode())
    data = player.socket.recv(1024)  # in format x/y
    cords = data.decode().split("/")
    battlefield.draw(player.symbol,int(cords[0]),int(cords[1]))
    if battlefield.check_win(player.symbol):
        player.socket.send(f"you win\n".encode())
        return battlefield, True
    return battlefield, False


def lets_start_gaming():
    global player1
    global player2
    battlefield = game.Map()
    win = False
    while True:
        for player in [player1, player2]:
            if win:
                player.socket.sendall(f"You lost!".encode())
                return
            elif battlefield.check_tie():
                player1.socket.send(f"Tie!".encode())
                player2.socket.send(f"Tie!".encode())
                return
            battlefield, win = turn_of_game(player, battlefield)


def run():
    global player1, player2
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 12345))
    while True:
        rsp1, rsp2 = True, True
        thread1 = threading.Thread(target=connect_to_server, args=(s,))
        thread2 = threading.Thread(target=connect_to_server, args=(s,))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        print("all good")
        while rsp1 and rsp2:
            lets_start_gaming()
            player1.socket.send(f"want a rematch y/n".encode())
            rsp1 = player1.socket.recv(1024).decode() == 'y'

            player2.socket.send(f"want a rematch y/n".encode())
            rsp2 = player2.socket.recv(1024).decode() == 'y'
        player1.socket.close()
        player2.socket.close()


run()
