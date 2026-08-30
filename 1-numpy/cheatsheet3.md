## Array Operations

### Slicing
```python
# VECTORS
vec = np.array([1, 2, 3, 4, 5, 6])

# specific element
print(vec[0])
print(vec[2])

# indexing
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