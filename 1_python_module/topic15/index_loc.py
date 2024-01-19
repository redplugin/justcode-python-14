import pandas as pd

df = pd.read_csv("test_data/people.csv")

# print(df.loc[:3, 'Name'])

# print(df)
# print("================================")
df = df.set_index('Name')
# print(df)

print(df.loc["Frank":"Bob", ['City', 'Age']])
