"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите
код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить
8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на
доске, определите, есть ли среди них пара бьющих друг друга. Программа получает
на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если
ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
from random import randint


__all__ = ['check_queens', 'random_placement']

SIZE = 8

board = [[0 for i in range(SIZE)]for j in range(SIZE)]
cnt = 0
cnt2 = 0
all_solving = []


def set_queen(i, j):
    global cnt2
    cnt2 += 1
    for x in range(SIZE):
        board[x][j] += 1
        board[i][x] += 1
        # диагонали
        if 0 <= i + j - x < SIZE:
            board[i + j - x][x] += 1
        if 0 <= i - j + x < SIZE:
            board[i - j + x][x] += 1
    board[i][j] = -1  # выставляем ферзя


def remove_queen(i, j):
    for x in range(SIZE):
        board[x][j] -= 1
        board[i][x] -= 1
        # диагонали
        if 0 <= i + j - x < SIZE:
            board[i + j - x][x] -= 1
        if 0 <= i - j + x < SIZE:
            board[i - j + x][x] -= 1
    board[i][j] = 0  # пустая клетка


def print_position():
    global cnt
    global all_solving
    cnt += 1
    abc = 'abcdefgh'
    ans = []
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i + 1))
    # print(', '.join(ans))
    all_solving.append(', '.join(ans))


def solve(i):
    for j in range(SIZE):
        if board[i][j] == 0:
            set_queen(i, j)
            if i == 7:
                print_position()
            else:
                solve(i + 1)
            remove_queen(i, j)  # убираем ферзя


def check_queens(list_of_tuples):
    global all_solving
    abc = 'abcdefgh'
    placement = ""
    solve(0)
    for item in list_of_tuples:
        placement += abc[item[0]-1] + str(item[1]) + ", "
    placement = placement[:-2]
    print(placement)
    if placement in all_solving:
        return True
    return False


def random_placement() -> bool:
    placement_list = []
    for _ in range(1, SIZE+1):
        _col = randint(1, SIZE)
        _row = randint(1, SIZE)
        placement_list.append((_col, _row))
    # print(placement_list)
    return check_queens(placement_list)


def draw_chess_board(board_size: int) -> None:
    width = height = 8
    w1char = '■'
    h1char = '□'
    print()
    print('a b c d e f g h')
    for i in range(height):
        for j in range(width):
            if (i + j) % 2 == 0:
                print(w1char, end=' ')
            else:
                print(h1char, end=' ')
        print(board_size - i)
        print()
    print('a b c d e f g h')
    print('1 2 3 4 5 6 7 8'
          '')


if __name__ == '__main__':
    # solve(0)
    # print(cnt)
    # print(cnt2)
    print()
    draw_chess_board(8)
    print()
    print(check_queens(
        [(1, 1), (5, 2), (8, 3), (6, 4), (3, 5), (7, 6), (2, 7), (4, 8)]))
    print(check_queens(
        [(1, 1), (5, 2), (8, 4), (6, 4), (3, 5), (7, 6), (2, 7), (4, 8)]))