import pandas as pd  # Import the pandas module as name it as pd
import makeChart # Import chart creation as separate code blocks to keep page tidy
df = pd.read_csv("volunteer.csv") # Create a dataframe using the CSV file provided
print(df.info())

# Go through the dataframe and drop any row that the values 'Both sexes' in the 'Sex' column
for x in df.index:
    if df.loc[x, "Sex"] == "Both sexes":
        df.drop(x, inplace = True)
        print(f"Replaced...{x}")

# Drop this label as I don't need it for my data
df = df.drop(columns=['Statistic Label'])

# Drop this label as I don't need it for my data
df = df.drop(columns=['UNIT'])

print("========\n")
print(df.info())

# Drop any row with 'involved' in the title
df = df[df['Volunteering Activities'] != 'Total persons involved in one or more voluntary activity']

# Drop any row with 'involved' in the title
df = df[df['Volunteering Activities'] != 'Persons not involved in voluntary activity including not stated']

print("========\n")
print(df.info())


# Go through the dataframe and get totals for respondends male and female

for x in df.index:
    
    if df.loc[x, "Sex"] == "Male" and df.loc[x, "Volunteering Activities"] == "All persons":
        print("Total MALE resondents: ", df.loc[x, "VALUE"])
        total_male_respond = df.loc[x, "VALUE"]
    
    if df.loc[x, "Sex"] == "Female" and df.loc[x, "Volunteering Activities"] == "All persons":
        print("Total FEMALE resondents: ", df.loc[x, "VALUE"])
        total_female_respond = df.loc[x, "VALUE"]
        
print("\n")


# Drop those rows now that I have the dataset
# Otherwise this will skew my titles
for x in df.index:
    if df.loc[x, "Volunteering Activities"] == "All persons":
        df.drop(x, inplace = True)
        print(f"Replaced...{x}")

print("==========================")
print("MALE STATISTICS")
print("==========================")

# Calcualte the mean of all the male volunteers
subset_male = df[df["Sex"] == "Male"]

# Calculate the mean of the 'Sex' column for the filtered rows
mean_value_male = subset_male["VALUE"].mean()
print(f"The MEAN value of all male volunteers is {int(mean_value_male)}")

# Find the median (If I organised everything and sorted it, this would be in the middle)
median_value_male = subset_male["VALUE"].median()
print(f"The MEDIAN value of all male volunteers is {median_value_male}")

# Find the mode (the value most often occuring)
mode_value_male = subset_male["VALUE"].mode().iloc[0]
print(f"The MODE value of all male volunteers is {mode_value_male}")

# Find the range (max - min)
print("The MAX value is ", subset_male['VALUE'].max())
print("The MIN value is ", subset_male['VALUE'].min())
range_value_male = subset_male['VALUE'].max() - subset_male['VALUE'].min()
print(f"Therefore the range is {range_value_male}")

# Add values to a dictionary datatype

male_stats = {
    "Mean":mean_value_male,
    "Median":median_value_male,
    "Mode":mode_value_male,
    "Range":range_value_male
    }

print(male_stats)

print("==========================")
print("FEMALE STATISTICS")
print("==========================")

for x in df.index:
    if df.loc[x, "Volunteering Activities"] == "Social/charity":
        print(df.loc[x, "Sex"], "Social work: ", df.loc[x, "VALUE"])

df.to_csv("changed_data_set.csv")

makeChart.getTheData()
