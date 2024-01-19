import pandas as pd


df = pd.read_csv("test_data/people.csv")

# print(df.iloc[0])
# print(df.iloc[:3])
# print(df.iloc[:, 3])

# print(df.iloc[:3, 0])
# print(df.iloc[:3, [1, 0]])
# df = df.set_index('Name')
print(df.iloc[:3, [1, 0]])

