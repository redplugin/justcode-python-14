import pandas as pd

data = {
    'Yes': [45, 21, None],
    'No': [131, 2, 123]
}

data2 = {'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}

df = pd.DataFrame(data2)

s = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
# s = df.Bob

print(type(df))
print(df)
print("================================")
print(type(s))
print(s)





