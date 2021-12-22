c = list("_" * 9)
cx = c.count("x")
co = c.count("o")
c_ = c.count("_")
win = 0


def play():
    print("---------")
    print("| ", end="")
    for a in c[:3]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in c[3:6]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in c[6:9]:
        print(a, end=" ")
    print("|")
    print("---------")

def game_part():
    global win
    if c[0] == c[1] == c[2] != "_":
        print(c[0] + " wins")
        win += 1
    elif c[3] == c[4] == c[5] != "_":
        print(c[3] + " wins")
        win += 1
    elif c[6] == c[7] == c[8] != "_":
        print(c[6] + " wins")
        win += 1
    elif c[2] == c[4] == c[6] != "_":
        print(c[2] + " wins")
        win += 1
    elif c[0] == c[4] == c[8] != "_":
        print(c[0] + " wins")
        win += 1
    elif c[0] == c[3] == c[6] != "_":
        print(c[3] + " wins")
        win += 1
    elif c[1] == c[4] == c[7] != "_":
        print(c[4] + " wins")
        win += 1
    elif c[2] == c[5] == c[8] != "_":
        print(c[5] + " wins")
        win += 1
    elif c_ < 1:
        win += 1
        print("Draw")

play()
tried = "X"
while True:
    inp = input("Enter the coordinates: ")
    cc = list(inp)
    x, y = str(cc[2]), str(cc[0])
    if x.isalpha() or y.isalpha() or x == " " or y == " ":
        print("You should enter numbers!")
        continue
    elif y == "1":
        if x == "1":
            if c[0] != "X" and c[0] != "O":
                c[0] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if c[1] != "X" and c[1] != "O":
                c[1] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if c[2] != "X" and c[2] != "O":
                c[2] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "2":
        if x == "1":
            if c[3] != "X" and c[3] != "O":
                c[3] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if c[4] != "X" and c[4] != "O":
                c[4] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if c[5] != "X" and c[5] != "O":
                c[5] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "3":
        if x == "1":
            if c[6] != "X" and c[6] != "O":
                c[6] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if c[7] != "X" and c[7] != "O":
                c[7] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if c[8] != "X" and c[8] != "O":
                c[8] = tried
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("Coordinates should be from 1 to 3!")
        continue
    play()
    game_part()
    if win > 0:
        break
    if tried == "X":
        tried = "O"
    else:
        tried = "X"