def game_of_life(board):
    rows = len(board)
    cols = len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    copy_board = [row[:] for row in board]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < rows and 0 <= nj < cols:
                    live_neighbors += copy_board[ni][nj]

            if copy_board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 0
            else:
                if live_neighbors == 3:
                    board[i][j] = 1

    return board


board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]

print(game_of_life(board))
