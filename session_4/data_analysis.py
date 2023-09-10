# python is used for data analysis because of the extreme support of the 3rd part packages like pandas, numpy, matplotlib -for charts
# first thing to do is to install the 3rd party packages (pip3 install pandas, etc.)

import pandas as pd
import matplotlib.pyplot as plt
# if this fails to run, type - python3 data_analysis.py (the file you intend to run)

bestsellers = pd.read_csv("bestsellers with categories.csv")
# to clean the data - removde duplicates
bestsellers = bestsellers.drop_duplicates(subset="Name", keep="last") 

# print(bestsellers) # this will prouce a dataframe

# Create a bar chart howing the author with the most amount of bestselling titles in the given years
# Create a pie chart shping the author with the distribution between fiction and non-fiction books


# no_of_bestsellers_written = bestsellers.groupby("Author")[["Name"]].count().sort_values("Name", ascending=False).head(10).reset_index()

# print(no_of_bestsellers_written)

# plt.bar(
#     no_of_bestsellers_written.Author, 
#     no_of_bestsellers_written.Name,
#     color="maroon",
#     width=0.4
#     )
# plt.xlabel("Authors")
# plt.ylabel("No of best sellers")
# plt.title("My first chart")
# plt.show()


distribution = bestsellers.groupby("Genre")[["Name"]].count().sort_values("Name", ascending=False).reset_index()
print(distribution)

plt.pie(
    distribution.Name,
    labels=distribution.Genre,
    autopct="%1.1f%%"
)
plt.show()