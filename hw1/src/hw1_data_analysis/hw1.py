import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the CSV file into a pandas dataframe.
df = pd.read_csv("bicycle_data.csv")

#2. In a comment, describe the columns in the dataframe and what data types they should be.
# Date                                                                      str, should be an datetime
#Fremont Bridge Sidewalks, south of N 34th St Total, total bike number                    float64, should be an integer
#Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk, west bike number    float64, should be an integer
#Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk, east bike number    float64, should be an integer
#Counts are float64 because some rows are missing (NaN) and regular int can't hold NaN, so I use pandas' "Int64" type

#update the data 
df.columns = ["date", "total", "west", "east"]
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y %I:%M:%S %p")
df[["total", "west", "east"]] = df[["total", "west", "east"]].astype("Int64")


#3. Add columns to the dataframe containing:
df["total_e+w"] = df["east"] + df["west"]    #he total (East + West) bicycle count.
df["hour"] = df["date"].dt.hour     #The hour of the day.
df["year"] = df["date"].dt.year     #the year

#4. Create a new dataframe with the subset of data from the year 2016. (1pt)
df_2016 = df[df["year"] == 2016].copy()

#5.do something to make sure missing data does not impact parts 6 and 7
print(df_2016.isna().sum()) # find which part of the data is empty
# There is 1 time point with missing data in 2016: 2016-03-13 02:00

df_2016 = df_2016.dropna() #2am of 3-13 is daylight saving, so there should be no data, so just delete the missing one

#6. plot the counts by hour Add an appropriate title and name the axes and save the image to a file called counts_by_hour.png
hourly_counts = df_2016.groupby("hour")["total_e+w"].sum()

hourly_counts.plot(kind="bar")
plt.title("Fremont Bridge bicycle counts by hour of day (2016)")
plt.xlabel("Hour of day")
plt.ylabel("Total counts")
plt.tight_layout()
plt.savefig("counts_by_hour.png")

# 7. use python (and pandas) programming to computationally determine what is (on average) the busiest hour of the day. 
# In a comment in the code write out the busiest hour

hourly_mean = df_2016.groupby("hour")["total_e+w"].mean()
busiest_hour = hourly_mean.idxmax()

print("Busiest hour:", busiest_hour)
print("Average bikes:", hourly_mean.max())

# The busiest hour on average in 2016 is at 17:00, (5pm) (average at 399.0327868852459)

