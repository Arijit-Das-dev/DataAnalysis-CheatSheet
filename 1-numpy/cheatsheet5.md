# Statistical Operation

### sum
```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

total = np.sum(mat1)
with_col = np.sum(mat1, axis=0)
with_row = np.sum(mat1, axis=1)
```

### Min
```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

minimum_value = np.min(mat1)
with_col = np.min(mat1, axis=0)
with_row = np.min(mat1, axis=1)
```

### Max
```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

maximum_value = np.max(mat1)
with_col = np.max(mat1, axis=0)
with_row = np.max(mat1, axis=1)
```

### Average / mean
```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

average_value = np.mean(mat1)
with_col = np.mean(mat1, axis=0)
with_row = np.mean(mat1, axis=1)
```


### Standard Daviation
```python
mat1 = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

std_value = np.std(mat1)
with_col = np.std(mat1, axis=0)
with_row = np.std(mat1, axis=1)
```