import pandas as pd

df = pd.read_csv("data/sales.csv")
# print(df)
# print((df['Quantity']*df['Price']).sum())
# df['month'] = df['Date'].str[:7]
# res = df.groupby('month')[['Quantity', 'Price']].sum().reset_index()
# print(res)

result_custom_functions = df.groupby('Category').agg({
    'Price': [('1', 'max'), ('11', 'min'), ('111', 'count')],
    'Quantity': [('2', 'max'), ('22', 'min'), ('222', 'count')]
})

# print(result_custom_functions.columns.values)
result_custom_functions.columns = ['_'.join(col).strip() for col in result_custom_functions.columns.values]

print(result_custom_functions)
# print(res.loc[res['Quantity']].max())