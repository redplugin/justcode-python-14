# !./ 0-9 A-Z a-z
import pandas as pd

sales = pd.read_csv("data/sales.csv")
# 1
# res = (sales['Quantity'] * sales['Price']).sum()
# print(res)
# --------------------------------

# print(sales)
# Date -> Month = Date[:7]

sales['overall_price'] = sales['Price'] * sales['Quantity']
sales['Month'] = sales['Date'].str[:7]
# print(sales)

result = sales.groupby('Month')[['overall_price']].sum()
print(result)















