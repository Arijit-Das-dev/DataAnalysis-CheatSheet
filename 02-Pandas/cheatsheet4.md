# Column & row Transformation

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

## 3. Edit columns
- Before analysing dataset via columns, we have to fix errors in columns.

```python
# check errors

# select columns
df.columns

# check for special characters containing columns
df.columns[df.columns.str.contains(r'[^A-Za-z0-9]')]

# check for numbers 
df.columns[df.columns.str.contains(r'[0-9]')]

# check for upper case letters containing columns
df.columns[df.columns != df.columns.str.lower()]

# check for spaces
df.columns[df.columns != df.columns.str.strip()]
```

```python
# improve columns
df.columns = (df.columns
             .str.strip()
             .str.lower()
             .str.replace(' ', '_')
             .str.replace(r'[^A-Za-z0-9_]', '')
)
```

