# write your code here
import random
import sys

sys.setrecursionlimit(30)


class player:

    def turns(self):
        global calc, choice, matr_list
        calculate()
        try:
            coord()
            if matrix[int(j_coord) - 1][int(i_coord) - 1] != " ":
                print("This cell is occupied! Choose another one!")
                return self.turns()
        except ValueError:
            print("You should enter numbers!")
            return self.turns()
        except IndexError:
            print("Coordinates should be from 1 to 3!")
            return self.turns()
        else:
            if calc[9] % 2 == 0:
                matrix[int(j_coord) - 1][int(i_coord) - 1] = "X"
                choice.remove([int(j_coord) - 1, int(i_coord) - 1])
                matr_list[3 * (j_coord - 1) + (i_coord - 1)] = 'X'
                matr()
                calculate()
                win()
            else:
                matrix[int(j_coord) - 1][int(i_coord) - 1] = "O"
                choice.remove([int(j_coord) - 1, int(i_coord) - 1])
                matr_list[3 * (j_coord - 1) + (i_coord - 1)] = 'O'
                matr()
                calculate()
                win()


class ai_hard:
    def __init__(self, turn):
        self.turn = turn
        if self.turn == 1:
            self.dot = 'X'
            self.opponent = 'O'
        else:
            self.dot = 'O'
            self.opponent = 'X'

    def winning(self, lis, playing):
        if ((lis[0] == playing and lis[1] == playing and lis[2] == playing) or
                (lis[3] == playing and lis[4] == playing and lis[5] == playing) or
                (lis[6] == playing and lis[7] == playing and lis[8] == playing) or
                (lis[0] == playing and lis[3] == playing and lis[6] == playing) or
                (lis[1] == playing and lis[4] == playing and lis[7] == playing) or
                (lis[2] == playing and lis[5] == playing and lis[8] == playing) or
                (lis[0] == playing and lis[4] == playing and lis[8] == playing) or
                (lis[2] == playing and lis[4] == playing and lis[6] == playing)):
            return True
        else:
            return False

    def minimax(self, lis, playing):
        avail_spots = emptyindex(lis)
        best_move = 0
        if self.winning(lis, self.opponent):
            return {'score': -10}
        elif self.winning(lis, self.dot):
            return {'score': 10}
        elif len(avail_spots) == 0:
            return {'score': 0}
        moves = []
        for i in range(len(avail_spots)):
            move = {}
            move.update({'index': lis[avail_spots[i]]})
            lis[avail_spots[i]] = playing
            if playing == self.dot:
                result = self.minimax(lis, self.opponent)
                move['score'] = result['score']
            else:
                result = self.minimax(lis, self.dot)
                move['score'] = result['score']

            lis[avail_spots[i]] = move['index']
            moves.append(move)



        if playing == self.dot:
            best_score = -10000
            for i in range(len(moves)):
                if moves[i]['score'] > best_score:
                    best_score = moves[i]['score']
                    best_move = i

        else:
            best_score = 10000
            for i in range(len(moves)):
                if moves[i]['score'] < best_score:
                    best_score = moves[i]['score']
                    best_move = i
        return moves[best_move]

    def turns(self):
        a = self.minimax(matr_list, self.dot)
        val = a['index']
        matr_list[val] = self.dot
        matrix[val // 3][val % 3] = self.dot
        choice.remove([val // 3, val % 3])
        print('Making move level "hard"')
        matr()
        calculate()
        win()

class ai_medium:
    def __init__(self, turn):
        self.turn = turn
        if self.turn == 1:
            self.dot = 'X'
            self.win = 2
            self.lose = -2
        else:
            self.dot = 'O'
            self.win = -2
            self.lose = 2

    def turns(self):
        global calc, matr_list
        possible_win = int
        possible_lose = int
        calculate()
        counter = 0
        print('Making move level "medium"')
        for i in range(8):
            if calc[i] == self.win:
                possible_win = i
                if 0 <= i < 3:
                    for j in choice:
                        if j[0] == i:
                            matrix[i][j[1]] = self.dot
                            choice.remove([i, j[1]])
                            matr_list[3 * i + j[1]] = self.dot
                            matr()
                            counter += 1
                    break
                elif 3 <= i < 6:
                    for j in choice:
                        if j[1] == i - 3:
                            matrix[j[0]][i - 3] = self.dot
                            choice.remove([j[0], i - 3])
                            matr_list[3 * j[0] + (i - 3)] = self.dot
                            matr()
                            counter += 1
                    break
                elif i == 6:
                    for j in range(3):
                        if matrix[j][j] == ' ':
                            matrix[j][j] = self.dot
                            choice.remove([j, j])
                            matr_list[3 * j + j] = self.dot
                            matr()
                            counter += 1
                    break
                elif i == 7:
                    for z in range(3):
                        for x in range(3):
                            if z + x == 2:
                                if matrix[z][x] == ' ':
                                    matrix[z][x] = self.dot
                                    choice.remove([z, x])
                                    matr_list[3 * z + x] = self.dot
                                    matr()
                                    counter += 1
                    break

            elif calc[i] == self.lose:
                possible_lose = i
                if 0 <= i < 3:
                    for j in choice:
                        if j[0] == i:
                            matrix[i][j[1]] = self.dot
                            choice.remove([i, j[1]])
                            matr_list[3 * i + j[1]] = self.dot
                            matr()
                            counter += 1
                    break
                elif 3 <= i < 6:
                    for j in choice:
                        if j[1] == i - 3:
                            matrix[j[0]][i - 3] = self.dot
                            choice.remove([j[0], i - 3])
                            matr_list[3 * j[0] + (i - 3)] = self.dot
                            matr()
                            counter += 1
                    break
                elif i == 6:
                    for j in range(3):
                        if matrix[j][j] == ' ':
                            matrix[j][j] = self.dot
                            choice.remove([j, j])
                            matr_list[3 * j + j] = self.dot
                            matr()
                            counter += 1
                    break
                elif i == 7:
                    for z in range(3):
                        for x in range(3):
                            if z + x == 2:
                                if matrix[z][x] == ' ':
                                    matrix[z][x] = self.dot
                                    choice.remove([z, x])
                                    matr_list[3 * z + x] = self.dot
                                    matr()
                                    counter += 1
                    break

        if counter == 0:
            turn = random.choice(choice)
            matrix[turn[0]][turn[1]] = self.dot
            choice.remove([turn[0], turn[1]])
            matr_list[3 * turn[0] + turn[1]] = self.dot
            matr()
            calculate()
            win()
        calculate()
        win()


class ai_easy:
    def __init__(self, turn):
        self.turn = turn
        if self.turn == 1:
            self.dot = 'X'
            self.win = 2
            self.lose = -2
        else:
            self.dot = 'O'
            self.win = -2
            self.lose = 2

    def turns(self):
        global calc, matr_list
        turn = random.choice(choice)
        matrix[turn[0]][turn[1]] = self.dot
        choice.remove([turn[0], turn[1]])
        matr_list[3 * turn[0] + turn[1]] = self.dot
        print('Making move level "easy"')
        matr()
        calculate()
        win()


calc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matr_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

choice = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

matrix = [[], [], []]
for j in range(3):
    for i in range(3):
        matrix[j].append(' ')


def matr():
    print("---------")
    for j in range(3):
        print(f"| {matrix[j][0]} {matrix[j][1]} {matrix[j][2]} |")
    print("---------")


def emptyindex(lis):
    availspots = []
    for i in range(len(lis)):
        if lis[i] != 'X' and lis[i] != 'O':
            availspots.append(lis[i])
    return availspots


j_coord = int
i_coord = int


def coord():
    global j_coord, i_coord
    a, b = input("Enter the coordinates: ").split()
    j_coord = int(a)
    i_coord = int(b)


def calculate():
    global calc
    calc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for z in range(3):
        for x in range(3):
            if matrix[z][x] == "X":
                calc[z] += 1
                calc[3 + x] += 1
                calc[9] += 1
                calc[8] += 1
                if x == z:
                    calc[6] += 1
                if x + z == 2:
                    calc[7] += 1
            elif matrix[z][x] == "O":
                calc[z] -= 1
                calc[3 + x] -= 1
                calc[9] += 1
                calc[8] -= 1
                if x == z:
                    calc[6] -= 1
                if x + z == 2:
                    calc[7] -= 1
    for x in range(8):
        if calc[x] == 3:
            calc[10] += 1
        if calc[x] == -3:
            calc[11] -= 1


def win():
    global calc
    if calc[10] > 0:
        print("X wins")
        menu()
    elif calc[11] < 0:
        print("O wins")
        menu()
    elif calc[9] == 9:
        print("Draw")
        menu()


def check():
    global calc, choice
    calculate()
    try:
        coord()
        if matrix[int(j_coord) - 1][int(i_coord) - 1] != " ":
            print("This cell is occupied! Choose another one!")
            check()
    except ValueError:
        print("You should enter numbers!")
        check()
    except IndexError:
        print("Coordinates should be from 1 to 3!")
        check()
    else:
        if calc[9] % 2 == 0:
            matrix[int(j_coord) - 1][int(i_coord) - 1] = "X"
            choice.remove([int(j_coord) - 1, int(i_coord) - 1])
            matr()
            calculate()
            win()
        else:
            matrix[int(j_coord) - 1][int(i_coord) - 1] = "O"
            choice.remove([int(j_coord) - 1, int(i_coord) - 1])
            matr()
            calculate()
            win()


def menu():
    global matrix, choice, calc, player_1, player_2, matr_list

    matrix = [[], [], []]
    matr_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    choice = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    for j in range(3):
        for i in range(3):
            matrix[j].append(' ')
    calculate()

    inp = list(input('Input command: ').split())
    if inp[0] == 'exit':
        exit()
    elif len(inp) != 3:
        print('Bad parameters!')
        menu()
    elif inp[0] == 'start':

        if inp[1] == 'user':
            player_1 = player()
        elif inp[1] == 'easy':
            player_1 = ai_easy(1)
        elif inp[1] == 'medium':
            player_1 = ai_medium(1)
        elif inp[1] == 'hard':
            player_1 = ai_hard(1)
        if inp[2] == 'user':
            player_2 = player()
        elif inp[2] == 'easy':
            player_2 = ai_easy(2)
        elif inp[2] == 'medium':
            player_2 = ai_medium(2)
        elif inp[2] == 'hard':
            player_2 = ai_hard(2)
        matr()
        while calc[9] < 9:
            player_1.turns()
            player_2.turns()

    menu()


menu()

matr()

check()
