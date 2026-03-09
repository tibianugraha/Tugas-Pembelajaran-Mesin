# %%
import pandas as pd
from IPython.display import display

# %%
# reading the database
data = pd.read_csv("tips.csv")

# %%
# printing the top 10 rows
display(data.head(10))
# %%
import pandas as pd
import matplotlib.pyplot as plt
 
 # %%
# reading the database
data = pd.read_csv("tips.csv")
 
 # %%
# Adding Title to the Plot
plt.title("Scatter Plot")
 # %%
# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# %%
# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])
 # %%
plt.show()
# %%
