import pandas as pd

path = r'D:\dibimbing DE\git-assignment\dibimbing-belajar-github\username.csv'

def read_csv(path, sep=','):
    return pd.read_csv(path, sep=sep)

df = read_csv(path, sep=';')

print(df.describe())
