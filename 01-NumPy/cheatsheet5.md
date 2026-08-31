# Statistical Operation

### Sum
```python
mat = np.array([
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
mat = np.array([
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
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

maximum_value = np.max(mat1)
with_col = np.max(mat1, axis=0)
with_row = np.max(mat1, axis=1)
```

### Average / Mean
```python
mat = np.array([
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
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

std_value = np.std(mat1)
with_col = np.std(mat1, axis=0)
with_row = np.std(mat1, axis=1)
```


### Mode
```python
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])

mode_value = np.mode(mat1)
with_col = np.mode(mat, axis=0)
with_row = np.mode(mat, axis=1)
```


### Median
```python
mat = np.array([
        [5, 6, 10],
        [4, 98, 12],
        [56, 3, 22]
])
median = np.median(mat)
with_col = np.median(mat, axis=0) 
with_row = np.median(mat, axis=1)
```