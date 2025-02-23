import pandas as pd

# 2. Creating a DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)

df.head(2)
