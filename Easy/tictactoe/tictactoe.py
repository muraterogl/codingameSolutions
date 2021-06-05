import sys
import math

board = []

for i in range(3):
    line = input()
    board += list(line)

def tester(board):
    winningPoss = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for a,b,c in winningPoss:
        if board[a]=="O" and board[b]=="O" and board[c]=="O":
            return True
    return False


for i in range(9):
    if board[i] == ".":
        board[i] = "O"
        if tester(board):
            for j in range(0,9,3):
                print("".join(board[j:j+3]))
            exit()
        else:
            board[i] = "."
print("false")