# %%
import pandas as pd
from IPython.display import display

# Membaca data langsung dari internet
url_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
# (Kita pakai data penguin karena data student sering error diakses langsung)
# Data ini berisi spesies penguin, pulau, dan ukuran fisiknya.
data_penguin = pd.read_csv(url_data)

# Menampilkan 5 baris pertama (seperti di modul LoadFilePandas.py)
display(data_penguin.head(5))