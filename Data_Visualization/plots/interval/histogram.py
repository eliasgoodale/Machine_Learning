import pandas as pd
import matplotlib.pyplot as plot

customers = pd.read_csv("..\\..\\..\\data\\UK-Bank-Customers.csv", index_col=0)

#rich_customers_visual = customers[customers['Balance'] > 100000].plot.hist()
#balance_visual = customers['Balance'].plot.hist()
age_visual = customers['Age'].plot.hist()
plot.show()