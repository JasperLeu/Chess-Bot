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
    return board

def printBoard(board):
    print("  " + '\033[4m' + " "*25 + '\033[0m')
    for y in range(8):
        print(8-y, end=' ')
        for x in range(8):
            val = board[x, 7-y]
            print(Back.RESET + "|", end='')
            back = (x + y % 2) % 2
            print([Back.WHITE, Back.BLACK][back], end='')
            print([Fore.BLACK, Fore.WHITE][back], end='')
            side = int(val/abs(val)+1) if not val == 0 else 1
            piece = pieceNums[abs(val)]
            piece = "N" if piece == "Knight" else piece[0]
            print('\033[4m' + "B W"[side] + piece + '\033[0m', end='')
        print(Back.RESET + "|")
    letters = ""
    for l in range(8):
        letters += " " + "abcdefgh"[l] + " "
    print("  " + letters)


# ----------------------------------------------------MAIN FUNCTIONS----------------------------------------------------
def readMove(move):
    return ["abcdefgh".find(move[0]), int(move[1])-1, "abcdefgh".find(move[2]), int(move[3])-1]

def validMove(move, board):
    x1, y1, x2, y2 = move
    if not (0 <= x2 <= 7 and 0 <= y2 <= 7):
        return False
    if board[x1, y1] * board[x2, y2] > 0:
        return False
    return True

def getMoves(position, board):
    x, y = position
    moves = []
    piece = board[x, y]
    name = pieceNums[abs(piece)]
    if name == " ":
        return moves
    s = int(np.sign(piece))

    # Pawn
    if name == "Pawn":
        # Forward 1
        if 7 >= y + s >= 0 == board[x, y + s]:
            moves.append([x, y, x, y + s])
            # Forward 2
            start_row = 1 if s == 1 else 6
            if y == start_row and board[x, y + 2 * s] == 0:
                moves.append([x, y, x, y + 2 * s])
        # Taking
        for dx in [-1, 1]:
            nx = x + dx
            ny = y + s
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx, ny] * piece < 0:
                    moves.append([x, y, nx, ny])
    # Knight
    elif name == "Knight":
        for dx, dy in [[-1, 2], [1, 2], [-1, -2], [1, -2], [2, -1], [2, 1], [-2, -1], [-2, 1]]:
            move = [x, y, x + dx, y + dy]
            if validMove(move, board):
                moves.append(move)
    # Bishop
    elif name == "Bishop":
        for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            for i in range(1, 8):
                nx, ny = x + dx * i, y + dy * i
                move = [x, y, nx, ny]
                if not validMove(move, board):
                    break
                moves.append(move)
                if board[nx, ny] != 0:
                    break
    # Rook
    elif name == "Rook":
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            for i in range(1, 8):
                nx, ny = x + dx * i, y + dy * i
                move = [x, y, nx, ny]
                if not validMove(move, board):
                    break
                moves.append(move)
                if board[nx, ny] != 0:
                    break
    # Queen
    elif name == "Queen":
        for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]:
            for i in range(1, 8):
                nx, ny = x + dx * i, y + dy * i
                move = [x, y, nx, ny]
                if not validMove(move, board):
                    break
                moves.append(move)
                if board[nx, ny] != 0:
                    break
    # King
    elif name == "King":
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                move = [x, y, x + dx, y + dy]
                if validMove(move, board):
                    moves.append(move)

    return moves


# ----------------------------------------------------ANALYZE BOARD-----------------------------------------------------
def analyze(board):
    print('\033[4m' + "ANALYSIS" + '\033[0m')
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
    print(f"*TOTAL EVALUATION: {evaluation:+}")
    return evaluation
