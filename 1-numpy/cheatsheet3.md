## Array Operations

### 1. Slicing
```python
# VECTORS
vec = np.array([1, 2, 3, 4, 5, 6])

# specific element
print(vec[0])
print(vec[2])

# indexing
print(vec[0:2]) # [1, 2]
print(vec[0:3]) # [1, 2, 3]
```

```python
# MATRIX
mat = np.array([

#   c-0 c-1 c-2
    [1,  2,  3],  # r - 0
    [4,  5,  6],  # r - 1
    [7,  8,  9]   # r - 2
])

# specific element
print(mat[0, 0])    # 1
print(mat[0, 2])    # 3

# indexing - used for getting specific rows and columns
print(mat[0:1, 0:4]) # [1,  2,  3]
print(mat[0:3, 1:2]) # [2,  5,  8]
```


### 2. Sorting
```python
# VECTOR
vec = [5, 12, 34, 9, 100, 87]
print(np.sort(vec))


# MATRIX - (axis= 0, 1)
# 0 - columns, 1 - row
mat = np.array([
    [
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
    ]
])
print(np.sort(mat, axis=0)) # by column
print(np.sort(mat, axis=1)) # by row
print(np.sort(mat))         # by row
```