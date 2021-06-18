import pandas as pd

read_file = pd.read_csv (r'F:\SOB\mempool.csv',delimiter=',')
read_file.to_csv (r'F:\SOB\block.txt', index=None)
print("successfully created")
