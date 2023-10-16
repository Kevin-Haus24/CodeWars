def chess_board(rows, columns):
    x, board = [], []
    for y in range(columns):
        for i in range(rows):
            if i == 0 or i % 2 == 0:
                x.append('O')
            else:
                x.append('X')
        board = [x]
    return board

print(chess_board(1, 2))