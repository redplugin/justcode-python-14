import pandas as pd


data1 = {
    "name1": ['Max', 'Male', 'John'],
    "age": [12, 34, 7]
}

data2 = {
    "name": ['Max', 'John', "Arai"],
    "gender": ["Male", "Male", "Female"]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# df1.set_index("name")
# df2.set_index("name")

print("df2")
print(df1)
print("================================================")
print("df2")
print(df2)

# result = pd.merge()
result = df1.merge(df2, how="outer", left_on="name1", right_on="gender")
# result = df1.join(df2, on="name", lsuffix="_x", rsuffix="_y", how="left")

# print("\n result ================================================")
# print(result)

# result = pd.concat([df1, df2], axis=1)
print("\n================================================")
print(result)

# result = pd.concat([df1, df2], axis=0)
# print("\n================================================")
# print(result)








