import sys

import numpy as np


class Pieces:
    global static_list

    def __init__(self, positions, m_n):
        self.positions = [item for item in positions]
        self.curr_pos = [item for item in positions[0]]
        self.prev_pos = []
        self.next_pos = []
        self.horizontal_moves = 0
        self.rotate_count = 0
        self.total_moves = 0
        self.max_width = m_n[0]
        self.max_height = m_n[1]
        self.touched_left = False
        self.touched_right = False
        self.touched_bottom = False
        self.static = False

    def print(self):
        for k in range(4):
            for i in range(self.max_height):
                for j in range(self.max_width):
                    if grid[i][j] == self.curr_pos[k]:
                        empty_grid[i][j] = '0'
        print()
        for line in empty_grid:
            print(' '.join(line))
        self.refresh()
        print()

    def rotate(self):
        # if len(self.positions) == 4:
        self.rotate_count += 1
        self.total_moves += 1
        if self.rotate_count == len(self.positions):
            self.rotate_count = 0
        if self.touched_bottom:
            pass
        else:
            self.curr_pos = self.positions[self.rotate_count]
            self.curr_pos = [item + self.horizontal_moves + self.max_width * self.total_moves for item in self.curr_pos]
        self.check_sides()

    def left(self):
        self.total_moves += 1
        self.horizontal_moves -= 1
        self.prev_pos = [item for item in self.curr_pos]
        for i in range(4):
            if self.touched_left and not self.touched_bottom:
                self.curr_pos[i] += self.max_width
            elif self.touched_bottom:
                break
            else:
                self.curr_pos[i] += -1 + self.max_width
        self.check_sides()

    def right(self):
        self.total_moves += 1
        self.horizontal_moves += 1
        self.prev_pos = [item for item in self.curr_pos]
        for i in range(4):
            if self.touched_right and not self.touched_bottom:
                self.curr_pos[i] += self.max_width
            elif self.touched_bottom:
                break
            else:
                self.curr_pos[i] += 1 + self.max_width
        self.check_sides()

    def down(self):
        if self.touched_bottom:
            self.check_sides()
        else:
            self.prev_pos = [item for item in self.curr_pos]
            self.total_moves += 1
            self.next_pos = [item + self.max_width for item in self.curr_pos]
            self.is_static()
            if not self.static:
                self.curr_pos = [item + self.max_width for item in self.curr_pos]

            self.check_sides()

    def check_sides(self):
        count_left = 0
        count_right = 0
        if self.touched_bottom:
            self.static = True
        for i in range(4):
            if self.curr_pos[i] % 10 == 0:
                self.touched_left = True
                count_left += 1
            elif self.curr_pos[i] % 10 == 9:
                self.touched_right = True
                count_right += 1
            if (self.curr_pos[i] // self.max_width) + 1 == self.max_height:
                self.touched_bottom = True
                # self.static = True
        if self.static:
            static_list.extend(self.curr_pos)

        if count_left < 1:
            self.touched_left = False
        if count_right < 1:
            self.touched_right = False

    def is_static(self):
        for i in range(4):
            if self.next_pos[i] in static_list:
                self.static = True

    def refresh(self):
        global empty_grid
        empty_grid = np.array([['-' for _ in range(self.max_width)] for _ in range(self.max_height)])
        for k in enumerate(static_list):
            for i in range(self.max_height):
                for j in range(self.max_width):
                    if grid[i][j] == k[1]:
                        empty_grid[i][j] = '0'


def print_empty():
    for line in empty_grid:
        print(' '.join(line))


grid_values = input().split()
grid_values = list(map(int, grid_values))
empty_grid = np.array([['-' for _ in range(grid_values[0])] for _ in range(grid_values[1])])
static_list = []
static_list = list(set(static_list))
grid = np.array([[x + grid_values[0] * i for x in range(grid_values[0])] for i in range(grid_values[1])])
O = [[4, 14, 15, 5]]
I = [[4, 14, 24, 34], [3, 4, 5, 6]]
S = [[5, 4, 14, 13], [4, 14, 15, 25]]
Z = [[4, 5, 15, 16], [5, 15, 14, 24]]
L = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
J = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
T = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]


def piece_inp():
    global new_piece
    inp = input()
    if inp == 'O':
        new_piece = Pieces(O, grid_values)
        new_piece.print()
    elif inp == 'I':
        new_piece = Pieces(I, grid_values)
        new_piece.print()
    elif inp == 'S':
        new_piece = Pieces(S, grid_values)
        new_piece.print()
    elif inp == 'Z':
        new_piece = Pieces(Z, grid_values)
        new_piece.print()
    elif inp == 'L':
        new_piece = Pieces(L, grid_values)
        new_piece.print()
    elif inp == 'J':
        new_piece = Pieces(J, grid_values)
        new_piece.print()
    elif inp == 'T':
        new_piece = Pieces(T, grid_values)
        new_piece.print()


def game_over():
    global grid_values
    count_line = 0
    count = 0
    for j in range(grid_values[0]):
        count = 0
        for i in enumerate(empty_grid):
            if i[1][j] == '0':
                count += 1
            if count == grid_values[1]:
                count_line += 1

    if count_line > 0:
        # print()
        print()
        sys.exit('Game over!')


def break_line():
    global static_list, grid_values, empty_grid
    num = []
    for j in range(grid_values[1]):
        if '-' in empty_grid[j]:
            pass
        else:
            num.append(j)
    for y in enumerate(num):
        for i in range(grid_values[0]):
            static_list.remove(grid[y[1]][i])
    static_list = [item + grid_values[0] for item in static_list]
    empty_grid = np.array([['-' for _ in range(grid_values[0])] for _ in range(grid_values[1])])
    for k in enumerate(static_list):
        for i in range(grid_values[1]):
            for j in range(grid_values[0]):
                if grid[i][j] == k[1]:
                    empty_grid[i][j] = '0'
    print_empty()


print_empty()

while True:
    # if new_piece:
    #     if new_piece.static:
    #         print(static_list)
    #         del new_piece
    command = input()
    if command == 'piece':
        piece_inp()
    elif command == 'rotate':
        new_piece.rotate()
        new_piece.print()
    elif command == 'left':
        new_piece.left()
        new_piece.print()
    elif command == 'right':
        new_piece.right()
        new_piece.print()
    elif command == 'down':
        new_piece.down()
        new_piece.print()
    elif command == 'exit':
        sys.exit()
    elif command == 'break':
        break_line()
    game_over()
    try:
        if new_piece.static:
            del new_piece
    except NameError:
        pass

