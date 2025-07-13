# often we want to group our data, and then do something specific to the group the data is in.

import pandas as pd

data = {
    "store": ['A', 'B', 'A', 'B', 'A', 'B'],
    "sales": [100, 200, 150, 300, 120, 250]
}

df = pd.DataFrame(data)

grouped = df.groupby('store')['sales'].sum()
print(grouped)