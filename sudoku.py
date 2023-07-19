def remove_available(available, board, row, col):
    num = board[row][col]

    # removing in same col
    for row2 in range(9):
        if num in available[row2][col] and board[row2][col] == '.':
            available[row2][col].remove(num)

    for col2 in range(9):
        if num in available[row][col2] and board[row][col2] == '.':
            available[row][col2].remove(num)

    offset_row = row // 3
    offset_col = col // 3
    for r in range(3):
        for c in range(3):
            if num in available[r + 3 * offset_row][c + 3 * offset_col] and board[r + 3 * offset_row][
                c + 3 * offset_col] == '.':
                available[r + 3 * offset_row][c + 3 * offset_col].remove(num)


def calculate_available(board):
    available = [[{"1", "2", "3", "4", "5", "6", "7", "8", "9"} for col in range(9)] for row in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue

            remove_available(available, board, row, col)
            available[row][col] = [board[row][col]]
    return available


def find_min_loc(board, available):
    min_set_len = 10
    min_set_loc = (-1, -1)
    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                continue

            s = available[row][col]
            if len(s) < min_set_len:
                min_set_len = len(s)
                min_set_loc = (row, col)

    if min_set_len == 10:
        return None
    return min_set_loc


def wave_function_collapse(board, available):
    min_loc = find_min_loc(board, available)
    if min_loc is None:
        return True  # solved

    min_r, min_c = min_loc
    min_set = available[min_r][min_c]
    if len(min_set) == 0:
        return False

    # save for restoring
    available_copy = [[col.copy() for col in row] for row in available]

    for option in min_set:
        # choose
        board[min_r][min_c] = option
        remove_available(available, board, min_r, min_c)
        if wave_function_collapse(board, available):
            return True

        # restore bc it didnt work
        board[min_r][min_c] = '.'
        for row in range(9):
            for col in range(9):
                available[row][col] = available_copy[row][col]

    return False


def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    available = calculate_available(board)
    print(available)
    wave_function_collapse(board, available)

def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solveSudoku(board)
    print(board)

if __name__ == '__main__':
    main()