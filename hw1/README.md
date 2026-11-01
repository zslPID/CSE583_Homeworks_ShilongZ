## Setup

I made the hw1 folder with the src and hw1_data_analysis folders inside, created the empty files, and added the pyproject.toml. Then I downloaded the data with curl and added a .gitignore so the csv file doesn't get uploaded to GitHub.

## Process

First I read the csv into a pandas dataframe and looked at the columns. I did some research and got help from AI on figuring out which data type each column should be. The date was read as text, so I changed it to datetime, I learned this from the bonus and do some web searching on this. And the bike counts were decimals because of missing values, so I changed them to integers. The date format in the data was different from the hint, so I had to use a different format to convert it.

Next I added columns for the East + West total, the hour, and the year, and made a new dataframe with only the 2016 data. In 2016 there was 1 missing data point, at 2 AM on March 13. With help from AI I tried out different ways to get rid of the NA data, like filling it with 0 or dropping it. I decided to drop it, because that hour didn't really exist: it was the day daylight saving time started and the clock jumped from 2 AM to 3 AM.

Last, I grouped the data by hour to make the plot, and used the average count for each hour to find the busiest hour.


## Datetime Formats

I converted the whole date column to the pandas datetime format. The three common formats are:

- datetime.datetime: Python's built-in format. Easy to use, but slow with lots of data.
- numpy datetime64: stores dates as numbers, so it's fast, but harder to work with.
- pandas Timestamp: built on numpy, so it's fast and also easy to get the hour or year from.
