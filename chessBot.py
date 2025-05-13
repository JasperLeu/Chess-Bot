#                          A CHESS BOT THAT IS VERY BAD AT CHESS (completely intentional)
# ----------------------------------------------------------------------------------------------------------------------
# Imports
import numpy as np
from colorama import Fore, Back

# ---------------------------------------------CONSTANTS / DICTIONARIES-------------------------------------------------
# + is white, - is black, 0 is empty
# Square key:
pieceNums = np.array([" ", "Pawn", "Knight", "Bishop", "Rook", "Queen", "King"])
materialDict = {"Pawn": 1, "Knight": 3, "Bishop": 3, "Rook": 5, "Queen": 9}
factorWeights = {"Material": 1, "Control": 1, "Structure": 1, "King Safety": 1.5}

# -------------------------------------------------BOARD FUNCTIONS------------------------------------------------------
def setupBoard():
    board = np.zeros((8, 8), dtype=np.int8)
    for side in [1, -1]:
        for pawn in range(8):
            y = np.int8(3.5 + 2.5 * -side)
            board[y, pawn] = side
        y = np.int8(3.5 + 3.5 * -side)
        board[y, 0] = 4 * side
        board[y, 7] = 4 * side
        board[y, 1] = 2 * side
        board[y, 6] = 2 * side
        board[y, 2] = 3 * side
        board[y, 5] = 3 * side
        board[y, 3] = 5 * side
        board[y, 4] = 6 * side
    return board

def printBoard(board):
    print("  " + f"\033[4m{" "*25}\033[0m")
    for y in range(8):
        print(8-y, end=' ')
        for x in range(8):
            val = board[-1-y, x]
            print(Back.RESET + "|", end='')
            back = (x + y % 2) % 2
            print([Back.WHITE, Back.BLACK][back], end='')
            print([Fore.BLACK, Fore.WHITE][back], end='')
            side = int(val/abs(val)+1) if not val == 0 else 1
            piece = pieceNums[abs(val)]
            piece = "N" if piece == "Knight" else piece[0]
            print(f"\033[4m{"B W"[side] + piece}\033[0m", end='')
        print(Back.RESET + "|")
    letters = ""
    for l in range(8):
        letters += " " + "abcdefgh"[l] + " "
    print("  " + letters)


# ----------------------------------------------------MAIN FUNCTIONS----------------------------------------------------
def validMove(move, board):
    pass


# ----------------------------------------------------ANALYZE BOARD-----------------------------------------------------
def analyze(board):
    print(f"\033[4m{""}\033[0m")
    evaluation = 0
    material = 0
    for y in range(8):
        for x in range(8):
            piece = abs(board[y, x])
            if 0 < piece < 6:
                side = np.int8(board[y, x] / piece)
                material += materialDict[pieceNums[piece]] * side
    print(f"Material: {material:+}")

    # Get final evaluation
    evaluation += material * factorWeights["Material"]
    print(f"* BOARD EVALUATION: {evaluation:+}")
    print(f"\033[4m{" "*27}\033[0m\n")
    return evaluation
