# %% 
#import pandas
import pandas as pd   

#load dataset to pandas dataframe
df = pd.read_csv("https://raw.githubusercontent.com/punyanith/cereal/main/cereal.csv") 

#the .head() display first 5 rows of the data
df.head()   
# %%
#determine data types of each column and see which columns have missing data
df.info()  

# %%
from numpy.lib.function_base import median
df[["calories", "sugars", "fiber", "fat", "protein"]].describe()
# %%
# How many cereals are in each brand
# Display the count of values for the manufacturer code ("mfr" column), then 
# create a new column containing the appropriate manufacturer names
# grouping the brands together
df['mfr_names'] = df["mfr"].map({'A': 'American Home Food Products', 'G': 'General Mills', 'K': 'Kelloggs','N': 'Nabisco', 'P': 'Post', 'Q': 'Quaker Oats', 'R': 'Ralston Purina'})
df['mfr_names'].value_counts()
# %%
# Import visual library
import altair as alt 
# %%
## what is the sugar content in all the cereals
# A bar graph showing the sugar content in all cereals

bar_chart = alt.Chart(df).mark_bar().encode( 
  x = alt.X('sugars', bin=True, axis = alt.Axis(title = 'Sugars')),
  y = alt.Y('count()', axis = alt.Axis(title = 'Count of Records'))).properties(
      title = {'text': 'Sugars Content in all Cereals'}
  )
bar_chart
# %%
## What is the relationship between sugar and calories

# A scatter plot showing the relationship between sugar and calories.
sc_chart = alt.Chart(df).mark_circle(size=60).encode(
      x = alt.X('sugars', axis = alt.Axis(title = 'Sugars')),
      y = alt.Y('calories', axis = alt.Axis(title = 'Calories'))).properties(
      title = {'text': 'Relationship of Sugars and Calories'}
  )
sc_chart

# %%
## What is the sugar content by manufacture
# A box plot showing the distribution of sugar content by manufacture.

box_chart = alt.Chart(df).mark_boxplot(extent='min-max').encode(
    x = alt.X('sugars', axis = alt.Axis(title = 'Sugars Content')),
      y = alt.Y('mfr', axis = alt.Axis(title = 'Manufacture'))).properties(
      title = {'text': 'Sugars Content by Manufacture'}
)
box_chart
# %%
