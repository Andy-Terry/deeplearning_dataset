import os
import numpy as np
m
if __name__ == "__main__":
    size_Distribution_output = np.zeros((3, 4))
    size_Distribution_output[0][1] = 12
    size_Distribution_output[2][0] = 33
    print(size_Distribution_output)
    print(size_Distribution_output.shape)
    a=8
    b=6
    matrix = size_Distribution_output.shape
    delta_rows = a - matrix[0]
    delta_columns = b - matrix[1]
    delta_rows_matrix = np.ones((delta_rows, b))
    # delta_rows_matrix = np.twos((a, delta_columns))
    delta_columns_matrix = np.ones((matrix[0], delta_columns))
    size_Distribution_output = np.c_[size_Distribution_output, delta_columns_matrix]
    size_Distribution_output = np.r_[size_Distribution_output, delta_rows_matrix]
    print(size_Distribution_output)
    print(size_Distribution_output.shape)
