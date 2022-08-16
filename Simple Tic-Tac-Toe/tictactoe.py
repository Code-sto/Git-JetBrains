# write your code here
calc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix = [[], [], []]
Xplayer = "X"
Oplayer = "O"
for j in range(3):
    for i in range(3):
        matrix[j].append(" ")


def matr():
    print("---------")
    for j in range(3):
        print(f"| {matrix[j][0]} {matrix[j][1]} {matrix[j][2]} |")
    print("---------")


j_coord = int
i_coord = int


def coord():
    global j_coord, i_coord
    a, b = input().split()
    j_coord = int(a)
    i_coord = int(b)


def calculate():
    global calc
    calc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for z in range(3):
        for x in range(3):
            if matrix[z][x] == "X":
                calc[z] += 1
                calc[3+x] += 1
                calc[9] += 1
                calc[8] += 1
                if x == z:
                    calc[6] += 1
                if x + z == 2:
                    calc[7] += 1
            elif matrix[z][x] == "O":
                calc[z] -= 1
                calc[3+x] -= 1
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


def check():
    try:
        coord()
        if matrix[int(j_coord)-1][int(i_coord)-1] != " ":
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
            matrix[int(j_coord)-1][int(i_coord)-1] = "X"
            matr()
            calculate()
            if calc[10] > 0:
                print("X wins")
                exit()
            elif calc[11] < 0:
                print("O wins")
                exit()
            elif calc[9] == 9:
                print("Draw")
                exit()
            check()
        else:
            matrix[int(j_coord)-1][int(i_coord)-1] = "O"
            matr()
            calculate()
            if calc[10] > 0:
                print("X wins")
                exit()
            elif calc[11] < 0:
                print("O wins")
                exit()
            elif calc[9] == 9:
                print("Draw")
                exit()
            check()



matr()
check()



rows_count = 0
columns_count = 0
if calc[10] + abs(calc[11]) > 1:
    for var in calc[0:3]:
        if abs(var) == 3:
            rows_count += 1
    for var in calc[3:6]:
        if abs(var) == 3:
            columns_count += 1

    if rows_count or columns_count > 1:
        print("Impossible")
elif abs(calc[8]) > 1:
    print("Impossible")
elif calc[10] > 0:
    print("X wins")
elif calc[11] < 0:
    print("O wins")
elif calc[9] == 9:
    print("Draw")
else:
    print("Game not finished")
