# Handling Missing & Duplicate Values

## 1. Handling Missing Values
- There are three data types of columns.
    - Numeric (integer)
    - object  (string)
    - date time

- If a column contains around 50 % Null values then identify why those rows contains null values. if there is no specific reason then you can simply drop that column.

### A. Numeric type Column
- For numeric columns -
    - Get total null values
    - If null percentage >= 50% , drop that column.
    - if percentage 20 - 30% , Check outlier
    - If outlier present - use median
    - If no outlier - use mean

```python

# 1. Get total null values
df.isnull().sum()                       # total missing values
df.isnull().sum() * 100 / df.shape[0]   # missing percentage

# 2. Check outlier if missing percentage (20 - 30 %)
def is_outlier(df: pd.DataFrame, column: str):
    Q1 = df[column].quantile(0.25)
    Q2 = df[column].median()
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    upper_limit = Q3 + (IQR * 1.5)
    lower_limit = Q1 + (IQR * 1.5)

    if len(df.loc[df[column] > upper_limit]) > 0 or len(df.loc[df[column] < lower_limit]) > 0:
        return True
    else:
        return False

if is_outlier(df=df, column=column):
    df[column] = df[column].replace(np.nan, df[column].median())
else:
    df[column] = df[column].replace(np.nan, df[column].mean())

# 3. If null percentage >= 50 %
df.drop(columns = [columns], inplace=True)
```

### B. Object type columns
- For object type column,
    - Get the percentage of null values
    - If null percentage >= 50 % , identify why it is missing.
    - If there is any specific reason of missing, then replace those    null rows with 'unknown'.
    - If no specific reason found then simply drop it.
    - If missing percentage is 5 to 20% then replace it with the **most frequent value**.

```python

# 1. Get total null values
df.isnull().sum()                       # total missing values
df.isnull().sum() * 100 / df.shape[0]   # missing percentage

# option 1 - missing percentage ( 5-10%)
df[column] = df[column].replace(np.nan, df[column].mode())

# option 2 - missing percentage (20 % - 50 % or below)
df[column] = df[column].fillna('unknown')
# or
df[column].fillna('unknown', inplace=True)

# option 3 - missing percentage ( > 50 % )
df.drop(columns=[column], inplace=True)
```