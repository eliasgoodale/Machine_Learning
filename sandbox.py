import pandas as pd
from Pandas.GroupBy.gb_extensions import gb_print

pd.core.groupby.generic.DataFrameGroupBy.print = gb_print


customers = pd.read_csv(".\\data\\UK-Bank-Customers.csv")

s = customers.groupby('Name')


# Return a series wherin the key of each index is the value of the key of the dataframe is specified.


s.print()
