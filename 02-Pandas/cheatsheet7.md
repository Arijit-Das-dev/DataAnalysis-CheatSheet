# Sorting
- Sorting is used to sort the numerical values in ascending or discending order.

## Example :
```python
import pandas as pd

df = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Arijit', 'Rahul', 'Priya', 'Amit', 'Sneha'],
    'Region': ['East', 'West', 'North', 'South', 'East'],
    'Unit_Price': [100, 150, 200, 120, 180]
})

df.sort_values(by='Unit_Price', ascending=True)
df.sort_values(by='Unit_Price', ascending=False)
```