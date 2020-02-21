import pandas as pd
df = pd.read_csv('/home/suraj/Desktop/MySQL/data/LEADS.csv', nrows=19)

for name, dtype in df.dtypes.iteritems():
    print(name, dtype)

