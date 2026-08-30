# Explore arrays/matrices/tensors

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

# diagonal matrix
diag = np.diag((2, 3))

# ones matrix
ones = np.ones(shape=(2, 3))

# full matrix
full = np.full((2, 3), 3)
```

## Creation of arrays
```python

# generate random numbers withing a given range of a fixed size
random_int = np.random.randint((low=1, high=5, size=12))


# generate random numbers of fixed size
random = np.random.random(size=12)


# create vector
vec = np.arange(1, 6)


# create matrix
mat = np.arange(1, 7).reshape(3, 2)


# other functions

flatten = mat.flatten()
ravel = flatten.ravel()
```