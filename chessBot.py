#                          A CHESS BOT THAT IS VERY BAD AT CHESS (completely intentional)
# ----------------------------------------------------------------------------------------------------------------------
# Imports
import numpy as np
from colorama import Fore, Back

# ----------------------------------------------CONSTANTS---------------------------------------------------------------
PAWN_VAL = 1
KNIGHT_VAL = 3
BISHOP_VAL = 3.5
ROOK_VAL = 5
QUEEN_VAL = 9
# + is white, - is black, 0 is empty
# Square key:
# 0=EMPTY, 1=Pawn, 2=Knight, 3=Bishop, 4=Rook, 5=Queen, 6=Queen

# ----------------------------------------------------SETUP BOARD-------------------------------------------------------
board = np.zeros((8, 8), dtype=np.int8)
def setupBoard():
    for side in [1, -1]:
        for pawn in range(8):
            y = np.int8(3.5 + 2.5 * -side)
            board[pawn, y] = side
        y = np.int8(3.5 + 3.5 * -side)
        board[0, y] = 4 * side
        board[7, y] = 4 * side
        board[1, y] = 2 * side
        board[6, y] = 2 * side
        board[2, y] = 3 * side
        board[5, y] = 3 * side
        board[3, y] = 5 * side
        board[4, y] = 6 * side

# ----------------------------------------------------DISPLAY BOARD-----------------------------------------------------
def printBoard():
    print("  " + f"\033[4m{" "*25}\033[0m")
    for y in range(8):
        print(8-y, end=' ')
        for x in range(8):
            val = board[x][-1-y]
            print(Back.RESET + "|", end='')
            back = (x + y % 2) % 2
            print([Back.WHITE, Back.BLACK][back], end='')
            print([Fore.BLACK, Fore.WHITE][back], end='')
            side = int(val/abs(val)+1) if not val == 0 else 1
            print(f"\033[4m{"B W"[side] + " PNBRQK"[abs(val)]}\033[0m", end='')
        print(Back.RESET + "|")
    letters = ""
    for l in range(8):
        letters += " " + "abcdefgh"[l] + " "
    print("  " + letters)


# ----------------------------------------------------ANALYZE BOARD-----------------------------------------------------
def analyze():
    matDiff = 0
    for x in range(8):
        for y in range(8):
            continue