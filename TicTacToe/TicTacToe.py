c = list("_" * 9)
cx = c.count("x")
co = c.count("o")
c_ = c.count("_")
win = 0

def play():
    print("---------")
    print("| ", end="")
    for a in c[1:3]:
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