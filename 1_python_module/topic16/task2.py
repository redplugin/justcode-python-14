
import pandas as pd

sales = pd.read_csv("data/sales.csv")

# print(sales['Quantity'].max())

result = sales.groupby('Product')[['Quantity']].sum()

# result = result.sort_values('Quantity', ascending=False)
# print(result.iloc[0:3])

# result = result.reset_index()
# print(result)
# print("result:", result.max())
# result = result.reset_index()

print(result)
print("++++++++++++++++")
# print("idxmax: ", result['Quantity'].idxmax())
# print("max: ", result['Quantity'].max())
print(result.loc[result['Quantity'].idxmax()])









