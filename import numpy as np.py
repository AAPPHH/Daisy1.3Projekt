import numpy as np
import random

def get_chain(board, player_number):
        chain = []
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    chain.append((row_index, col_index))
        return chain

def direction(board, player_number):
    chain = get_chain(board, player_number)
    moves_list = []
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value == player_number:
                if (row_index, col_index+1) in chain:
                    print("right")
                    moves_list.append((row_index, col_index+2))
                elif (row_index, col_index-1) in chain:
                    print("left")
                    moves_list.append((row_index, col_index-2))
                elif (row_index+1, col_index) in chain:
                    print("down")
                    moves_list.append((row_index+2, col_index))
                elif (row_index-1, col_index) in chain:
                    print("up")
                    moves_list.append((row_index-2, col_index))
                elif (row_index+1, col_index+1) in chain:
                    print("downright")
                    moves_list.append((row_index+2, col_index+2))
                elif (row_index-1, col_index-1) in chain:
                    print("upleft")
                    moves_list.append((row_index-2, col_index-2))
                elif (row_index+1, col_index-1) in chain:
                    print("upright")
                    moves_list.append((row_index+2, col_index-2))
                elif (row_index-1, col_index+1) in chain:
                    print("downleft")
                    moves_list.append((row_index-2, col_index+2))
                else:
                    return "none"
    for i, j in moves_list:
        if 0 <= i < 5 and 0 <= j < 5: 
            moves_list.remove((i, j))
            return moves_list
board = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])

moves_list = direction(board, 1)
print(moves_list)
# row, col = random.choice(moves_list)
# # print(row)
# # print(col)
# board[row][col] = 1
# print(board)

# def find_chain_positions(board, player_number):
#     m, n = board.shape
#     chain_positions = []

#     for i in range(m):
#         for j in range(n):
#             if board[i][j] == player_number:
#                 # Überprüfen Sie alle benachbarten Positionen
#                 neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]  # Oben, unten, links, rechts
#                 for x, y in neighbors:
#                     if 0 <= x < m and 0 <= y < n:
#                         if board[x][y] == player_number:
#                             # Überprüfen Sie die diagonalen Nachbarn für eine mögliche 0
#                             diagonal_neighbors = [(i-1, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1)]
#                             for dx, dy in diagonal_neighbors:
#                                 if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 0:
#                                     chain_positions.append((dx, dy))

#     return chain_positions

# # Beispiel-Array
# #board = np.array([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])

# # Finden der Positionen, die eine Kette bilden
# positions = find_chain_positions(board, 1)
# print("Positionen, die eine Kette bilden:", positions)


