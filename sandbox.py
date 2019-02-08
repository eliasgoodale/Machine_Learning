import pandas as pd
from Pandas.GroupBy.gb_extensions import gb_print

pd.core.groupby.generic.DataFrameGroupBy.print = gb_print


reviews = pd.read_csv("./Pandas/data/UK-Bank-Customers.csv")
name_grouped = reviews.groupby('Name')


print(reviews[])
