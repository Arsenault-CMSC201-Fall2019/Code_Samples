# program to read in a game board as a single string
# then split it into individual characters
def split_board(board):

# board is a string that will be split into
# a 2-d list of characters

    l_b = board.split('\n')
    for i in range(len(l_b)):
        l_b[i] = list(l_b[i])
    return l_b

if __name__ == "__main__":
    with open("board.py","r") as f:
        board = f.read()
        s_board = split_board(board)
        print(s_board)

