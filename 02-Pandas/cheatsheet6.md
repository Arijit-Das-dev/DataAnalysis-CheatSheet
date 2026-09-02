# Merge (Join), Concatenate
- We use Merge function when we need to join multiple tables.
- Types of Merge (Joins),
    - ***INNER JOIN***
    - ***LEFT JOIN***
    - ***RIGHT JOIN***
    - ***OUTER JOIN***


```python
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Arijit', 'Rahul', 'Priya', 'Amit', 'Sneha'],
    'Region': ['East', 'West', 'North', 'South', 'East'],
    'Unit_Price': [100, 150, 200, 120, 180]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphone'],
    'Quantity': [2, 5, 3, 4, 6],
    'Discount': [10, 15, 5, 20, 12]
})
```

## 1. Merge
```python
inner_join = pd.merge(left=df1, right=df2, on='ID', how='inner')
left_join = pd.merge(left=df1, right=df2, on='ID', how='left')
right_join = pd.merge(left=df1, right=df2, on='ID', how='right')
outer_join = pd.merge(left=df1, right=df2, on='ID', how='outer')
```

## 2. Concat
```python
pd.concat([df1, df2], axis=1) # joins row wise
pd.concat([df1, df2], axis=0) # join column wise
```