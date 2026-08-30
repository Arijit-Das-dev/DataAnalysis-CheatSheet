import numpy as np

mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

mat2 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

new_row = [2, 3, 4]
print(np.vstack((mat1, mat2)))
print(np.hstack((mat1, mat2)))