import pandas as pd
import matplotlib.pyplot as plot

customers = pd.read_csv("../../../data/UK-Bank-Customers.csv", index_col=0)
visual = customers['Name'].value_counts().head(10) / len(customers)

visual.plot.bar()
plot.show()