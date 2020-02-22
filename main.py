import random
from enum import Enum
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


class HitStatus(Enum):
    HAS_HIT = -2
    MISS = -1
    HIT = 0
    KILLED = 1


LEGEND = {
    'EMPTY': ' ',
    'MISS': '0',
    'SHIP': '=',
    'HIT': '#',
}


class Ship:
    def __init__(self, *, size: int, coordinates: List[Tuple[int, int]]):
        self.size = size,
        self.coordinates = coordinates
        self.hits = 0


class BattleshipBoard:
    def __init__(self, *, name: str, height: int = SIZE[0], width: int = SIZE[1]):
        self.name = name
        self._ships = []
        self.height = height - 1
        self.width = width - 1
        self.board = [[LEGEND['EMPTY'] for _ in range(height)] for _ in range(width)]
        self.enemy_board = [[LEGEND['EMPTY'] for _ in range(height)] for _ in range(width)]
        self.ships_count = 0

        for ship, count in SHIPS_COUNT_DICT.items():
            for x in range(count):
                self.set_ship(ship_size=SHIPS_SIZE_DICT[ship])

    def set_ship(self, ship_size: int) -> None:
        founded: List[Tuple[int, int]] = []

        while True:
            if len(founded) == ship_size:
                for n_x, n_y in founded:
                    self.board[n_x][n_y] = LEGEND['SHIP']
                    self.ships_count += 1

                return

            founded = []

            x = random.randint(0, self.height)
            y = random.randint(0, self.width)

            desired_size = ship_size

            tilt = random.randint(0, 1)
            if tilt == 0:
                while desired_size > 0:
                    for i in range(x, x + ship_size):
                        if self.has_neighbors(x=i, y=y):
                            break
                        founded.append((i, y))
                        desired_size -= 1

                    for i in range(x - ship_size, x - 1):
                        if self.has_neighbors(x=i, y=y):
                            break
                        founded.append((i, y))
                        desired_size -= 1

                    break

            elif tilt == 1:
                for i in range(y, y + ship_size):
                    if desired_size > 0:
                        if self.has_neighbors(x=x, y=i):
                            break
                        founded.append((x, i))
                        desired_size -= 1

                for i in range(y - ship_size, y - 1):
                    if desired_size > 0:
                        if self.has_neighbors(x=x, y=i):
                            break

                        founded.append((x, i))
                        desired_size -= 1

                    break

    def check_hit(self, x, y) -> HitStatus:
        if x < 0 or y < 0:
            return HitStatus.MISS

        if x > self.height or y > self.width:
            return HitStatus.MISS

        val = self.get_value(x, y)
        if val == LEGEND['HIT']:
            return HitStatus.HAS_HIT

        if val != LEGEND['SHIP']:
            return HitStatus.MISS

        self.ships_count -= 1
        self.board[int(x)][int(y)] = LEGEND['HIT']

        if not self.has_neighbors(x=x, y=y):
            return HitStatus.KILLED

        return HitStatus.HIT

    def get_value(self, x: int, y: int) -> str:
        if x < 0 or y < 0:
            return LEGEND['EMPTY']
        if x > self.height or y > self.width:
            return LEGEND['EMPTY']

        return self.board[x][y]

    def has_neighbors(self, *, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return True

        if x > self.height or y > self.width:
            return True

        if self.get_value(x, y) == LEGEND['SHIP']:
            return True

        if x - 1 >= 0:
            if y - 1 >= 0:
                if self.get_value(x - 1, y - 1) == LEGEND['SHIP']:
                    return True
            if self.get_value(x - 1, y) == LEGEND['SHIP']:
                return True

        if x + 1 < self.height:
            if y + 1 < self.width:
                if self.get_value(x + 1, y + 1) == LEGEND['SHIP']:
                    return True
            if self.get_value(x + 1, y) == LEGEND['SHIP']:
                return True

        if y + 1 < self.width:
            if self.get_value(x, y + 1) == LEGEND['SHIP']:
                return True
            if x - 1 >= 0:
                if self.get_value(x - 1, y + 1) == LEGEND['SHIP']:
                    return True

        if x + 1 < self.height:
            if self.get_value(x + 1, y) == LEGEND['SHIP']:
                return True
            if y - 1 >= 0:
                if self.get_value(x + 1, y - 1) == LEGEND['SHIP']:
                    return True

        return False

    def print_board(self):
        for i in range(self.width):
            print(self.board[i], '      |      ', self.enemy_board[i])


def get_input(player_name: str) -> Tuple[int, int]:
    cells = input(f'{player_name}\'s turn: X:Y').split(':')

    x = ord(cells[0].lower()) - 97

    return x, int(cells[1]) - 1


def main():
    player_1 = BattleshipBoard(name=input('Player 1 name:'))
    player_2 = BattleshipBoard(name=input('Player 2 name:'))

    while player_1.ships_count > 0 or player_2.ships_count > 0:
        while True:
            player_1.print_board()
            # x, y = get_input(player_1.name)

            x = random.randint(0, player_1.height)
            y = random.randint(0, player_1.width)
            print(x, y)

            has_hit = player_2.check_hit(int(x), int(y))
            if has_hit == HitStatus.MISS:
                player_1.enemy_board[int(x)][int(y)] = LEGEND['MISS']
                print('Miss!')
                break
            if has_hit in (HitStatus.HIT, HitStatus.KILLED):
                player_1.enemy_board[int(x)][int(y)] = LEGEND['HIT']

                if has_hit == HitStatus.KILLED:
                    print('Killed!')
                else:
                    print('Hit!')

                if player_2.ships_count == 0:
                    print(f'{player_1.name} wins!')
                    return

        while True:
            player_2.print_board()
            # x, y = get_input(player_2.name)

            x = random.randint(0, player_1.height)
            y = random.randint(0, player_1.width)
            print(x, y)

            has_hit = player_1.check_hit(int(x), int(y))
            if has_hit == HitStatus.MISS:
                player_2.enemy_board[int(x)][int(y)] = LEGEND['MISS']
                print('Miss!')
                break
            if has_hit in (HitStatus.HIT, HitStatus.KILLED):
                player_2.enemy_board[int(x)][int(y)] = LEGEND['HIT']

                if has_hit == HitStatus.KILLED:
                    print('Killed!')
                else:
                    print('Hit!')

            if player_1.ships_count == 0:
                print(f'{player_1.name} wins!')
                return


if __name__ == "__main__":
    main()
