#!/usr/bin/python3
'''Solving N queens'''
import sys


def is_safe(board, row, col):
    '''Checks if placing a queen at (row, col) is safe'''
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    '''Solves the N queens problem using backtracking'''
    if col >= len(board):
        solution = [i for row in board for i, v in enumerate(row) if v == 1]
        print(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1)
            board[i][col] = 0


def main():
    '''Main function'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()
