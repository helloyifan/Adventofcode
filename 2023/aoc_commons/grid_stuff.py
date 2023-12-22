def rotate_matrix(matrix):
    # Transpose the matrix (swap rows with columns)
    transposed_matrix = list(zip(*matrix))

    # Reverse the order of rows to complete the rotation
    rotated_matrix = [list(row)[::-1] for row in transposed_matrix]

    return rotated_matrix

def rotate_matrix_counterclockwise(matrix):
    # Reverse each row
    reversed_rows = [row[::-1] for row in matrix]

    # Transpose the matrix (swap rows with columns)
    rotated_matrix = list(zip(*reversed_rows))

    return rotated_matrix


def is_valid_index(grid, row_index, col_index):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1 if grid else -1  # Handle empty grid case

    return 0 <= row_index <= max_row and 0 <= col_index <= max_col