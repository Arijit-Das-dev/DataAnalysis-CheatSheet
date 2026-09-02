# GROUP BY
- Group by function is used to combine mutliple dupicate rows into one row.
- Simply it combines multiple category into single one.
- It is heavily used with statistical / aggregate function for analysis.

## Example
```python
df.groupby('gender')['gender'].count()

df.groupby('product')['sales'].sum()

df.groupby('Department')['employee_id'].count()

df.groupby('Department')['salary'].mean()

df.groupby('Department')['salary'].max()
```

```python
# applying multiple aggregate functions at once
df.groupby('region')['sales'].agg(['mean', 'min', 'max', 'sum'])

df.groupby('Department')['salary'].agg(['mean', 'min', 'max', 'sum'])
```