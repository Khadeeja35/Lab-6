#   "Khadeeja Bibi and Dorcas Bola"

#                                        PART 3

# 1) 

# Question 1: How does the population size vary by region?
# Question 2: How does women represetation in parliament vary by subregion?
# Question 3: Is there a association between gas emission per capita and life expectancy?

# 2) 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("wdi_wide.csv")

# 3)

df.info()

# Answer: There are 10 empty values for the column "Physicians" and 
#         0 empty values for the "Population" column.

# 4)

df.nunique()
print(df.nunique())

# Answer: This command is used to find the number of unique values in each column.
#         For example, when we run it, we can see that there is 5 different regions, 
#         217 different countries, etc. in the data set.

# 5)

df.describe()
print(df.describe())

# Answer: The output of this function provide us the descriptive statistics 
#         of the dataset (mean, standard deviation, etc.)

# 6)

df["GNI per capita"] = df["GNI"]/df["Population"]
print(df["GNI per capita"].round())

# Answer: The output of this function give us the GNI per person because 
#         we have a lot of data we use the average of GNI per person.

# 7)

  # a)

country_count = df["Region"].value_counts()
print(country_count)

# Answer: There are 54 countries in Africa, 50 countries in Asia, 47 in Europe, 
#         46 in Americas and 19 in Oceania. 

  # b)

high_income_count = df["High Income Economy"].value_counts()
print(high_income_count)

# Answer: There are 67 high income economies.

# 8)

high_income_economy = pd.crosstab(df["Region"],df["High Income Economy"])
print(high_income_economy)

# There is 17 high income economy in Americas, 14 in Asia, 31 in Europe and 4 in Oceania.

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

# Answer: There are 66 countries where women can expect to live for more than 80 years.


#                                           PART 4

# 1) 

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, female", 
            y = "GNI per capita", 
            kind = "scatter", 
            height = 5, 
            aspect = 1.5)
plt.title ("Association between GNI per capita and Female Life Expectancy")

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, male", 
            y = "GNI per capita", 
            kind = "scatter", 
            height = 5, 
            aspect = 1.5)
plt.title ("Association between GNI per capita and Male Life Expectancy")

# Answer: Yes, there is a positive association between GNI per capita and 
#         life expectancy for both men and women. From the graph we can see that 
#         as GNI per capita increases, life expectancy also tend to increase. 
#         This means that richer countries have higher life expectancy because 
#         they have better healthcare systems, higher education levels, etc.
#         Also, the female life expectancy tends to be slightly higher than 
#         male life expectancy.

# 2)

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, female", 
            y = "GNI per capita", 
            hue = "Region", 
            kind = "scatter", 
            height = 5, 
            aspect = 1.5)
plt.title("GNI per capita vs Female Life Expectancy by Region")

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, male", 
            y = "GNI per capita", 
            hue = "Region", 
            kind = "scatter", 
            height = 5, 
            aspect = 1.5)
plt.title("GNI per capita vs Male Life Expectancy by Region")

# Answer: Yes, the association between GNI per capita and life expectancy does 
#         vary by region for both men and women. From the previous question, 
#         we saw that there is a positive relationship between GNI per capita 
#         and life expectancy. However, this relationship differ by regions:
#         In Africa, there is low GNI per capita and low life expectancy.
#         In Europe, there is high GNI per capita and high life expectancy.
#         In Oceania, Asia and Americas, it is mainly moderate for both GNI 
#         per capita and life expectancy

# 3)

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.relplot(data = df,
            x= "Life expectancy, female",
            y = "GNI per capita", 
            hue = "Region",
            kind = "scatter",
            height = 5, 
            aspect = 1.5)
plt.title("GNI per capita vs Female Life Expectancy by Region")

# 4)

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.lmplot(data = df,
            x= "Life expectancy, female",
            y = "GNI per capita", 
            hue = "Region",
            height = 5, 
            aspect = 1.5)
plt.title("GNI per capita vs Female Life Expectancy by Region")

# 5)

# Comparing Female Tertiary Education and Female Life Expectancy by region

sns.relplot(data = df, 
            x= "Life expectancy, female", 
            y = "Tertiary education, female", 
            kind = "scatter", 
            col = "Region",
            height = 5, 
            aspect = 1.5)
plt.title("Female Tertiary education vs Female Life Expectancy by region")

# Comparing Male Tertiary Education and Male Life Expectancy by region

sns.relplot(data = df, 
            x= "Life expectancy, male", 
            y = "Tertiary education, male", 
            kind = "scatter", 
            col = "Region",
            height = 5, 
            aspect = 1.5)
plt.title("Male Tertiary education vs Male Life Expectancy by region")

# Comparing Gas Emission per capita and Female Life Expectancy by region

df["emission per capita"] = df["Greenhouse gas emissions"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, female", 
            y = "emission per capita", 
            kind = "scatter",
            col = "Region",
            height = 5, 
            aspect = 1.5)
plt.title("Emission per capita vs Female Life Expectancy by region")

# Comparing Gas Emissions per capita and Male Life Expectancy by region

df["emission per capita"] = df["Greenhouse gas emissions"] / df["Population"]
sns.relplot(data = df, 
            x= "Life expectancy, male", 
            y = "emission per capita",  
            kind = "scatter",
            col = "Region",
            height = 5, 
            aspect = 1.5)
plt.title("Emission per capita vs Male Life Expectancy by region")

# Answer: By exploring some female life expectancy relationship with some of 
#         the other numerical feature, we see that for male life expectancy, 
#         these relationshsip are the same for both.

# Question 1: How does internet use vary across regions?

sns.barplot(data = df, 
            x= "Region", 
            y = "Internet use",)
plt.title("Internet use by Region")

# Answer: Europe has the most internet users compared to Africa which has the less internet users.

# Question 2: Which subregion has the most GNI per capita?

df["GNI per capita"] = df["GNI"] / df["Population"]
sns.barplot(data = df, 
            x= "Subregion", 
            y = "GNI per capita")
plt.title("GNI per capita by Subregion")
plt.xticks(rotation=90)

# Answer: Western Europe and Northern America have the most GNI per capita.

# Question 3: How does women’s representation in parliament vary by region?

sns.barplot(data = df, 
            x = "Region", 
            y = "Women in national parliament")
plt.title("Women in National Parliament by Region")
plt.xticks(rotation=90)

# Answer: Regions like Europe and Americas have more women in parliament comapred to 
#         Oceania who have few women in their parliament.

# Question 4: Which region has the most international tourism?

sns.barplot(data = df, 
            x= "Region", 
            y = "International tourism")
plt.title("International Tourism by Region")

# Answer: Europe has the highest level of international tourism.

# Question 5 : How does the population size vary among regions?
    
sns.barplot(data = df, 
            x= "Region", 
            y = "Population")
plt.title("Population by Region")

# Answer: Asia is the region with the most population while Oceania with the less population.

# 6)

  # a)

df["emission per capita"] = df["Greenhouse gas emissions"] / df["Population"]
sns.relplot(data = df, 
            x= "Internet use", 
            y = "emission per capita", 
            kind = "scatter", 
            height = 5, 
            aspect = 1.5)
plt.title("Emission per capita vs Internet Use")

# Answer: There isn't a clear association between the internet use and emission per capita. 

  # b) 

df["emission per capita"] = df["Greenhouse gas emissions"] / df["Population"]
high_emissions_countries = df[df["emission per capita"] > 0.03]
print(high_emissions_countries)

# Answer: The countries that have high gas emissions are Brunei Darussalam and 
#         Qatar both situated in the same region, Asia.

  # c)

# Answer: From b) we found out that Brunei Darussalam and Qatar were the region 
#         that had high emissions. Since they are both in the same region, 
#         there is no variation.

  # d)

# Answer: From PART 3 question 7) b), we found that there is 67 high income economies 
#         and from PART 4 question 6) b), we found that there is only 2 countries 
#         that have high gas emissions. Thus, no not all high income economies 
#         have high gas emissions. However, both countries that have high gas emissions 
#         also have high income economies.