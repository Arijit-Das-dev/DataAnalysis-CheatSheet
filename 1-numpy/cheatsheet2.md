## Explore arrays/matrices/tensors
```python
import numpy as np
matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print("Dimension : ", matrix.ndim)  # 2-D
print("Shape : ", matrix.shape)     # (3, 3)
print("Size : ", matrix.size)       # 9
print("Type : ", matrix.dtype)      # int64
```

## Types of Matrices
```python
# zeros matrix
zeros = np.zeros((2, 3))


# identity matrix
eye = np.eye(N=3, M=3)  # N = Rows, M= Columns
print(eye)


# diagonal matrix
diag = np.diag((2, 3))
print(diag)


# ones matrix
ones = np.ones(shape=(2, 3))
print(ones)


# full matrix
full = np.full((2, 3), 3)
print(full)
```