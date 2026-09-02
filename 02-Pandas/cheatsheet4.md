# Row & Column Transformation


## 1. Add new column
```python
df['bonus'] = df['salary'] * 0.1

# by condition
df.loc[(df['salary'] <= 10000), 'Bonus'] = df.loc[(df['salary'] <= 10000), 'salary'] * 0.1

df.loc[(df['gender'] == 'Female'), 'new_gender'] = 'F'

df.loc[(df['gender'] == 'Male'), 'new_gender'] = 'M'

df['full_name'] = df['First_name'] + df['Last_name']
```

## 2. Drop existing column
```python
df.drop(columns=['column1', 'column2'])
```