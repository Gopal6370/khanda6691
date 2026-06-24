import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("ecommerce_data.csv")

print(df.columns)

print(df["Gender"].value_counts())

male = df[df["Gender"] == "Male"]["Purchase_Amount"]
female = df[df["Gender"] == "Female"]["Purchase_Amount"]

print("Male Samples:", len(male))
print("Female Samples:", len(female))

if len(male) > 1 and len(female) > 1:
    t_stat, p_value = ttest_ind(male, female)

    print("T Statistic:", t_stat)
    print("P Value:", p_value)
else:
    print("Not enough samples for hypothesis testing.")
    