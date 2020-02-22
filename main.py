import random
from typing import Tuple, List

SIZE = 10, 10
SHIPS_COUNT_DICT = {
    'battleship': 1,
    'cruiser': 2,
    'submarine': 3,
    'boat': 4,
}
SHIPS_SIZE_DICT = {
    'battleship': 4,
    'cruiser': 3,
    'submarine': 2,
    'boat': 1,
}


class Ship:
    def __init__(self, size: int, coordinates: List[Tuple[int, int]]):
        self.size = size,
        self.coordinates = coordinates
        self.hits = 0


class BattleshipBoard:
    def __init__(self, *, height: int=SIZE[0], width: int=SIZE[1]):
        self._ships = []
        self.height = height - 1
        self.width = width - 1
        self.board = [[' ' for _ in range(height)] for _ in range(width)]
        self.enemy_board = [[' ' for _ in range(height)] for _ in range(width)]
        self.ships_count = 0

        for ship, count in SHIPS_COUNT_DICT.items():
            for x in range(count):
                self.set_ship(ship_size=SHIPS_SIZE_DICT[ship])

    def set_ship(self, *, ship_size: int) -> None:
        founded: List[Tuple[int, int]] = []

        while True:
            if len(founded) == ship_size:
                for n_x, n_y in founded:
                    self.board[n_x][n_y] = '='
                    self.ships_count += 1

                return

            founded = []

            x = random.randint(0, self.height)
            y = random.randint(0, self.width)

            desired_size = ship_size

            tilt = random.randint(0, 1)
            if tilt == 0:
                while desired_size > 0:
                    for i in range(x, x+ship_size):
                        if self.has_neighbors(x=i, y=y):
                            break
                        founded.append((i,y))
                        desired_size -= 1

                    for i in range(x-ship_size, x-1):
                        if self.has_neighbors(x=i, y=y):
                            break
                        founded.append((i, y))
                        desired_size -= 1

                    break

            elif tilt == 1:
                for i in range(y, y+ship_size):
                    if desired_size > 0:
                        if self.has_neighbors(x=x, y=i):
                            break
                        founded.append((x, i))
                        desired_size -= 1

                for i in range(y-ship_size, y-1):
                    if desired_size > 0:
                        if self.has_neighbors(x=x, y=i):
                            break

                        founded.append((x, i))
                        desired_size -= 1

                    break

    def check_hit(self, x, y) -> int:
        if x < 0 or y < 0:
            return -1

        if x > self.height or y > self.width:
            return -1

        val = self.get_value(x, y)
        if val != '=':
            return -1

        self.ships_count -= 1
        self.board[int(x)][int(y)] = '#'

        if not self.has_neighbors(x=x,y=y):
            return 1

        return 0

    def get_value(self, x: int, y: int) -> str:
        if x < 0 or y < 0:
            return ' '
        if x > self.height or y > self.width:
            return ' '

        return self.board[x][y]

    def has_neighbors(self, *, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return True

        if x > self.height or y > self.width:
            return True

        if self.get_value(x, y) == '=':
            return True

        if x - 1 >= 0:
            if y - 1 >= 0:
                if self.get_value(x - 1, y - 1) == '=':
                    return True
            if self.get_value(x - 1, y) == '=':
                return True

        if x + 1 < self.height:
            if y + 1 < self.width:
                if self.get_value(x + 1, y + 1) == '=':
                    return True
            if self.get_value(x + 1, y) == '=':
                return True

        if y + 1 < self.width:
            if self.get_value(x, y + 1) == '=':
                return True
            if x - 1 >= 0:
                if self.get_value(x-1, y + 1) == '=':
                    return True

        if x + 1 < self.height:
            if self.get_value(x + 1, y) == '=':
                return True
            if y - 1 >= 0:
                if self.get_value(x + 1, y - 1) == '=':
                    return True

        return False

    def print_board(self):
        for i in range(self.width):
            print(self.board[i], '      |      ', self.enemy_board[i])


def main():
    player_1 = BattleshipBoard()
    player_2 = BattleshipBoard()
    while player_1.ships_count > 0 or player_2.ships_count > 0:
        while True:
            print('Player1 turn:')
            # x, y = input('Player1 turn:')
            player_1.print_board()
            x = random.randint(0, player_1.height)
            y = random.randint(0, player_1.width)
            print(x ,y)
            has_hit = player_2.check_hit(int(x), int(y))
            if has_hit == -1:
                player_1.enemy_board[int(x)][int(y)] = 'O'
                print('Miss!')
                break

            player_1.enemy_board[int(x)][int(y)] = '#'

            if has_hit == 1:
                print('Killed!')
            else:
                print('Hit!')

            if player_2.ships_count == 0:
                print('Player1 wins!')
                return

        while True:
            # x, y = input('Player2 turn:')
            print('Player2 turn:')
            player_2.print_board()
            x = random.randint(0, player_1.height)
            y = random.randint(0, player_1.width)
            print(x, y)
            has_hit = player_1.check_hit(int(x), int(y))
            if has_hit == -1:
                player_2.enemy_board[int(x)][int(y)] = 'O'
                print('Miss!')
                break

            player_2.enemy_board[int(x)][int(y)] = '#'

            if has_hit == 1:
                print('Killed!')
            else:
                print('Hit!')

            if player_1.ships_count == 0:
                print('Player1 wins!')
                return

    print('END')

if __name__ == "__main__":
    main()
