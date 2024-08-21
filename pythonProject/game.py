class Map:
    def __init__(self):
        self.map = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def draw(self, symbol, x, y):
        self.map[y][x] = symbol

    def check_collision(self, x, y):
        return self.map[y][x] != 0

    def check_win(self,symbol):
        for y in range(0,3):
            if self.map[y][0] == self.map[y][1] == self.map[y][2] == symbol:
                return True
            if self.map[0][y] == self.map[1][y] == self.map[2][y] == symbol:
                return True
        if self.map[0][0] == self.map[1][1] == self.map[2][2] == symbol:
            return True
        if self.map[0][2] == self.map[1][1] == self.map[2][0] == symbol:
            return True
        else:
            return False

    def check_tie(self):
        for y in range(0,3):
            for x in range(0,3):
                if self.map[y][x] == 0:
                    return False
        return True

    def display(self):
        return str(self.map).replace("], [", "]\n[")


class Player:
    def __init__(self, symbol, socket, addr):
        self.symbol = symbol
        self.socket = socket
        self.addr = addr
