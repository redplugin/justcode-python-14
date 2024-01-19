import pandas as pd

df = pd.read_csv("test_data/people.csv")
print(df)
# df["gt_30"] = df.Age > 30
# df = df.loc[df.City == 'Dallas']
# df = df.loc[(df.City== 'Dallas') & (df.Age >= 25)]
# df = df.loc[(df.City== 'Dallas') | (df.Age >= 30)]
# df = df.loc[~df.Gender.isnull()]
# df = df.loc[df.Gender.notnull()]

# print(df)

# print(df.City)
# print(df.City == 'Dallas')


