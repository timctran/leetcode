def printmatrix(matrix):
    matrix_str = ['\t'.join([str(cell) for cell in row]) for row in matrix]
    print(' '+'\n '.join(matrix_str))