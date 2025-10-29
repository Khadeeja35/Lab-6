#                                           PART 3

# 1) 

# Question 1: 
# Question 2:
# Question 3:

# 2) 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("wdi_wide.csv")

# 3)

df.info()

# Answer: There are 10 empty values for the column "Physicians" and 0 empty values for the "Population" column.

# 4)

df.nunique()
print(df.nunique())

# 5)

df.describe()
print(df.describe())

# Answer: The output of this function provide us the descriptive statistics of the dataset (mean, standard deviation, etc.)

# 6)

df["GNI per capita"] = df["GNI"]/df["Population"]
print(df["GNI per capita"].round())

# 7)

  # a)

country_count = df["Region"].value_counts()
print(country_count)

# Answer: There are 54 countries in Africa, 50 countries in Asia, 47 in Europe, 46 in Americas and 19 in Oceania. 

  # b)

high_income_count = df["High Income Economy"].value_counts()
print(high_income_count)

# Answer: There are 67 high income economies.

# 8)

high_income_economy = pd.crosstab(df["Region"],df["High Income Economy"])
print(high_income_economy)

# There is 17 high income economy in Americas, 14 in Asia, 31 in Europe and 4 in Oceania

# 9)

filtered_data = df[df["Life expectancy, female"] > 80]
print(filtered_data)

count = 0
countries = []

for i, row in df.iterrows():
    if row["Life expectancy, female"] > 80:
        count += 1
        countries.append(row["Country Name"])
print(countries)

# Answer: There are 66 countries where women can expect to live for more than 80 years


#                                           PART 4

# 1) 

sns.relplot(data = df, x= "Life expectancy, female", y = "GNI per capita", kind = "scatter", height = 5, aspect = 1.5)
plt.title ("Association between GNI per capita and Female Life Expectancy")
plt.show()

sns.relplot(data = df, x= "Life expectancy, male", y = "GNI per capita", kind = "scatter", height = 5, aspect = 1.5)
plt.title ("Association between GNI per capita and Male Life Expectancy")
plt.show()

# Answer: Yes, there is a positive association between GNI per capita and life expectancy for both men and women. 
#         From the graph we can see that as GNI per capita increases, life expectancy also tend to increase. 
#         This means that richer countries have higher life expectancy because they have better healthcare systems, higher education levels, etc.
#         Also, the female life expectancy tends to be slightly higher than male life expectancy.

# 2)

sns.relplot(data = df, x= "Life expectancy, female", y = "GNI per capita", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("GNI per capita vs Female Life Expectancy by Region")
plt.show()

sns.relplot(data = df, x= "Life expectancy, male", y = "GNI per capita", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("GNI per capita vs Male Life Expectancy by Region")
plt.show()

# Answer: Yes, the association between GNI per capita and life expectancy does vary by region for both men and women.
#         From the previous question, we saw that there is a positive relationship between GNI per capita and life expectancy.
#         However, this relationship differ by regions:
#         In Africa, there is low GNI per capita and low life expectancy.
#         In Europe, there is high GNI per capita and high life expectancy.
#         In Oceania, Asia and Americas, it is mainly moderate for both GNI per capita and life expectancy

# 3)



# 4)



# 5)

# Comparing Female Tertiary Education and Female Life Expectancy by region

sns.relplot(data = df, x= "Life expectancy, female", y = "Tertiary education, female", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("Female Tertiary education vs Female Life Expectancy by region")
plt.show()

# Comparing Male Tertiary Education and Male Life Expectancy by region

sns.relplot(data = df, x= "Life expectancy, male", y = "Tertiary education, male", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("Male Tertiary education vs Male Life Expectancy by region")
plt.show()

# Comparing Internet Use and Female Life Expectancy by region

sns.relplot(data = df, x= "Life expectancy, female", y = "Internet use", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("Internet use vs Female Life Expectancy by region")
plt.show()

# Comparing Internet Use and Male Life Expectancy by region

sns.relplot(data = df, x= "Life expectancy, male", y = "Internet use", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("Internet use vs Male Life Expectancy by region")
plt.show()

# Answer: By explore some female life expectancy relationship with some of the other numerical feature, 
#         we see that for male life expectancy, 
#         these relationshsip are the same for both.

# Question 1: Does GNI per capita relate to Internet use?

sns.relplot(data = df, x= "GNI per capita", y = "Internet use", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("GNI per capita vs Internet Use by Region")
plt.show()

# Question 2: Is there a relationship between GNI per capita and the number of physicians?

sns.relplot(data = df, x= "GNI per capita", y = "Physicians", hue = "Region", kind = "scatter", height = 5, aspect = 1.5)
plt.title("GNI per capita vs Physicians by Region")
plt.show()

# Question 3: How does women’s representation in parliament vary by subregion?

sns.barplot(data = df, x = "Subregion", y = "Women in national parliament")
plt.title("Women in National Parliament by Subregion")
plt.xticks(rotation=90)
plt.show()

# Question 4: Which region has the most international tourism?

sns.barplot(data = df, x= "Region", y = "International tourism")
plt.title("GNI per capita vs International Tourism by Region")
plt.show()

# Question 5 : How does the population size vary in region?
    
sns.barplot(data = df, x= "Region", y = "Population")
plt.title("Population by Region")
plt.show()
