
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv(r"C:\Users\ARUNKUMAR\OneDrive\Desktop\Zomato.csv")
dataframe['rate']
print(dataframe['rate'])
#-----------------Data Cleaning------------------
def handleRate(value):
    value = str(value).split('/')  
    value = value[0];
    return value
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe['rate'])
# ===========================================================

# =============================================================================
# 1.)What type of resturant  do the majority of customers order from?
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")

# Majority of the resturant falls in dinning category
# =============================================================================

# =============================================================================
# 2.)How many votes has each types of restaurant  received from customers?
 
group_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':group_data})
plt.plot(result, c="green", marker="+")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("votes", c="red", size=20)

# ==> Dining has recieved ajority votes 
# =============================================================================

# ====================================================
#3.)What are the rating  that majarity of restaurants  have received?

plt.hist(dataframe['rate'],bins=3)
plt.title("Ratings Distrubutions")
plt.show()

#==> The majority restaurnt recieved rating 3 to 4
# =================================================================================


# =================================================================================
# 4.)Average order spending couples order?
couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

#==> The majority of couples prefer approximate cost of 300
# =================================================================================


# =================================================================================
#5.)Which mode recieves maximum rating ?

plt.figure(figsize =(6,6))
sns.boxplot(x='online_order',y='rate',data = dataframe)

#==> Offline order recieved lower rating  in comparision 
# to online order
# ====================================================


