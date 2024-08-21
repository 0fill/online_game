import socket


def check_resp(resp, map):
    try:
        if int(resp[0]) in range(0, 3) and int(resp[2]) in range(0, 3):
            if resp[1] == '/':
                return True
        else:
            return False
    except:
        return False


def wait_for_fucking_massage(s):
    while True:
        msg = s.recv(1024)
        msg = msg.decode()
        if len(msg) > 1:
            return msg


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 12345))
while True:
    while True:
        msg = wait_for_fucking_massage(s)
        print(msg)
        if msg[0] != '[':
            break
        map = list(msg.split('\n')[0])
        myyy = True
        while myyy:
            resp = input(f"chose the cordinations x/y 0-2: ")
            if check_resp(resp, map):
                s.send(resp.encode())
                myyy = False
    while True:
        msg = wait_for_fucking_massage(s)
        resp = input(f"\n {msg}")
        if resp == 'y':
            s.send(resp.encode())
            break
        elif resp == 'n':
            s.send(resp.encode())
            s.close()
            quit()
