import pandas as pd


df = pd.read_csv("test_data/people.csv")
# df = pd.DataFrame([])

# print(df.shape)
# print(df.empty)
# print(df.head())
# print(df.City)
print(df["City"])
print(type(df["City"]))



