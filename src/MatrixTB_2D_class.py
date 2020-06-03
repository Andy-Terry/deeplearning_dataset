import os
import numpy as np

class MatrixTB_2D:
    def __init__(self):
        self.matrix_input = 0
        self.shape_input = 0

    def matrix_make(self, matrix_input, shape_input):
        matrix_output = matrix_input
        matrix_size = matrix_input.shape
        rows_new = shape_input[0]
        columns_new = shape_input[1]

        if columns_new > matrix_size[1]:
            delta_columns = columns_new - matrix_size[1]
            delta_columns_matrix = np.zeros((matrix_size[0], delta_columns))
            matrix_output = np.c_[matrix_output, delta_columns_matrix]

        if rows_new > matrix_size[0]:
            delta_rows = rows_new - matrix_size[0]
            delta_rows_matrix = np.zeros((delta_rows, columns_new))
            matrix_output = np.r_[matrix_output, delta_rows_matrix]

        return matrix_output