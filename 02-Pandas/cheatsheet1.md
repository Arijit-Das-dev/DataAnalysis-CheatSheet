# PANDAS
- Pandas used for Analyse massive amount of data with millions of rows and columns.
- It is used for data pre-processing tasks such as data sourcing, loading, cleaning, standardizing and analysing.
- It allows you to work with DataFrames.
- In pandas all the data stores in DataFrame format.
- Pandas is heavily used in many domains such as **Health Care**, **Finance**, **Neuroscience**, **statistics**, **Advertisin g & Web Analysis**.


## INSTALLATION
```python
# to install
pip install pandas

# to check version
pip show pandas
```

## Basic Fundamentals
```python

# create data frame
import pandas as pd

data = {
    "name": ['A', 'B', 'C', 'D', 'E'],
    "salary": [10000, 20000, 15000, 45000, 23000],
    "age": [22, 21, 23, 24, 34]
}

df = pd.DataFrame(data)
df


# read excel file 
df = pd.read_xlsx("data.xlsx")

# read csv file
df = pd.read_csv("data.csv")

# read sql file
df = pd.read_sql("data.sql")

# read html file
df = pd.read_html("data.html")

# read json file
df= pd.read_json("data.json")
```

## How to save data ?
```python

# to sql file
df = pd.read_xlsx("data.xlsx")
df.to_xlsx("data.xlsx")


# read csv file
df = pd.read_csv("data.csv")
df.to_cev("data.csv")


# read sql file
df = pd.read_sql("data.sql")
df.to_sql("data.sql")


# read html file
df = pd.read_html("data.html")
df.to_html("data.html")


# read json file
df = pd.read_json("data.json")
df.to_json("data.json")
```