board = [" "] * 9

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check():
    win = [(0,1,2), (3,4,5), (6,7,8),
           (0,3,6), (1,4,7), (2,5,8),
           (0,4,8), (2,4,6)]

    for a, b, c in win:
        if board[a] == board[b] == board[c] != " ":
            return True
    return False

player = "X"

for i in range(9):
    display()
    pos = int(input("Player " + player + " position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player

        if check():
            display()
            print(player, "wins!")
            break

        player = "O" if player == "X" else "X"
else:
    display()
    print("Draw!")\






