## Array Manupulation

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
- Sort all values in ascending or discending order.

```python
# VECTOR
vec = [5, 12, 34, 9, 100, 87]
print(np.sort(vec))


# MATRIX - (axis= 0, 1)
# 0 - columns, 1 - row
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])
print(np.sort(mat, axis=0)) # by column
print(np.sort(mat, axis=1)) # by row
print(np.sort(mat))         # by row
```


### 3. Filter
- For filtering we always use masking.
- It returns True and False.

```python
# VECTOR
vec = np.array([5, 12, 34, 9, 100, 87])
mask = vec > 10
print(vec[mask])


# MATRIX
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])
mask = mat > 10
print(mat[mask])

# we can use np.where() function also for filtering
mask = np.where(vec>10)
mask = np.where(mat>10)
```


### 4. Concatenation
- Concatenation means combining multiple arrays into one.

```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

mat2 = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
])
print(np.concatenate((mat1, mat2), axis=1))
print(np.concatenate((mat1, mat2), acis=0))


print(np.vstack((mat1, mat2)))
print(np.hstack((mat1, mat2)))
```


### 5. Deleting
- Deleting rows and columns.
- For deleting rows and columns, we consider axis,
- 0 = rows
- 1 = columns

```python
mat = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
])

deleted_row = np.delete(mat, 2, axis=0) # [7,  8,  9] (row)
deleted_col = np.delete(mat, 2, axis=1) # [3,  6,  9] (columns)
```


### 6. Inserting
- Inserting new row or column.

```python
mat = np.array([
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
])

inserted_row = np.insert(mat, 2, [23, 43, 12], axis=0)
inserted_col = np.insert(mat, 2, [1, 4, 5], axis=1)
```