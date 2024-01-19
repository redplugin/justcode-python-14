import pandas as pd

people = pd.read_csv("data/people.csv")

# select Gender, max(Age) from people group by 'Gender'
# max, min, sum, count, mean
res = people.groupby('Gender')[['Age', 'Name']].min()

res = res.reset_index()
print(res)




