import random, sys

sys.setrecursionlimit(2000)
grille = [[0] * 20 for i in range(20)]
pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
revele = [[0] * 20 for i in range(20)]


# functions
def output(g):
    for col in g: print(" ".join(map(str, col)))


def bombe():
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    grille[y][x] = "*"
    number(x, y)


def number(x, y):
    for c in pos:
        try:
            if grille[y + c[0]][x + c[1]] != "*":
                grille[y + c[0]][x + c[1]] += 1
        except:
            pass


def onclick(x, y):
    try:
        if grille[y][x] == "*":
            output()
            print("perdu")
            return 0
        if grille[y][x] != 0:
            revele[y][x] = 1
            return 1
        grille[y][x] = "@"
        revele[y][x] = 1
        for c in pos:
            onclick(x + c[0], y + c[1])
    except:
        pass


def main():
    for loop in range(int(20 * 20 * 0.15)):
        bombe()

    output(grille)
    print()
    m = onclick(14, 13)
    if m or m==None:
        output(revele)


