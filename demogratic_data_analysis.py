"""How many people of each race are represented in this dataset? This should be a Pandas series 
with race names as the index labels. (race column)
What is the average age of men?
"""

import pandas as pd

data = pd.read_csv("adult_data.csv")
race = data["race"]
age = data["age"]
cont = data["native-country"]

#race counts
race.value_counts()
race.count()

#average age of men
ave_men = round(sum(age[data["sex"] == "Male"]) / age[data["sex"] == "Male"].count(), 1)

#percentage of barcelor degree holders
edu = data["education"]
barc = edu[data["education"] == "Bachelors"]
per = round((barc.count() /edu.count()) * 100, 1)

#percentage of high income workers
sal = edu[data["salary"] == ">50K"]
bac = sal[data["education"] == "Bachelors"].count()
mas = sal[data["education"] == "Masters"].count()
doc = sal[data["education"] == "Doctorate"].count()
high_in_per = round(((bac+doc+mas) / edu.count()) * 100, 1)

#percentage of undergraduates with high income jobs
adv = sal.count() - (bac+doc+mas)
under_high_in_per = round(((adv) / edu.count()) * 100, 1)

#The minimum a person works per week
min_hr_per_wk = data["hours-per-week"].min()

#The lazy high income workers
laz = sal[data["hours-per-week"] == min_hr_per_wk].count()
l_hig_in_per = round(((laz) / edu.count()) * 100, 4)

#country with >50k
abv50 = cont[data["salary"] == ">50K"]
high_abv50_cont = abv50.mode() #United-States
high_cont = "United-States"
high_abv50_cont_per = round(((abv50[abv50 == "United-States"].count()) / edu.count()) * 100, 1)

#india most popular high income occupation
ind = data["occupation"][cont == "India"]
mor50 = ind[data["salary"] == ">50K"]
mos_pop_occ = mor50.mode()#Prof-specialty
mos_occ = "Prof-specialty"

print(f"Percentage of high income workers: {high_in_per}%", f"Average age of men: {ave_men}yrs",
f"Percentage of barcelor degree holders: {per}%", f"Race counts: \n{race.value_counts()}", 
f"Percentage of undergraduates with high income jobs: {under_high_in_per}%",
f"The minimum a person works per week: {min_hr_per_wk} hr/wk", f"The lazy high income workers percentage: {l_hig_in_per}%",
f"Country with highest >50k jobs: {high_cont}", f"Country with the highest >50k job percentage: {high_abv50_cont_per}%",
f"India most popular high income occupation: {mos_occ}", sep="\n")
