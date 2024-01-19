
import pandas as pd

sales = pd.read_csv("data/sales.csv")

# result = sales.groupby('Category')['Price'].mean()

result = sales.groupby('Category').agg({
    'Price': [('mean_of_price', 'mean'), ('sum_of_price', 'sum')],
    'Quantity': 'sum'
})

result.columns = [col[1] for col in result.columns.values]
print(result)

