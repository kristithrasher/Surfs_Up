# Surfs_Up

## Overview

The following is Data Analysis for a business investor, W. Avy. The business venture is for a potential surf and shake shack to be located in Oahu, Hawaii. He would like to know if the surf and shake shop business would be sustainable year round.  
W. Avy gave me a weather database in SQLite. He specifically wants temperature data for the months of June and December in Oahu, in order to dermine 
First step in analysis was to retrieve the temperature data for month of June in Oahu. I did this with the sqlite database provided entitled "hawaii.sqlite". I used Python, Pandas funtions and methods, and SQLAlchemy to filter the date column of the Measurements table in "hawaii.sqlite" to retrieve all the temperatures for the month of June and December. I then converted those temperatures to a list and created two seperate DataFrames entitled june_df and dec_df from the two lists to generate the summary statistics. 

## Deliverable 1
### Summary Statistics for the Month of June. 
The month of June showed the minimum temperature was 64 degrees, maximum temperature was 85 and the average as 74. 

![june_stats](https://user-images.githubusercontent.com/94208810/149611195-dc5f38b0-3f45-438e-8db6-209c215bf34a.png)

## Deliverable 2
### Summary Statistics for the Month of December. 
The Month of December showed the minimum temperature of 56 degrees, maximum temperature as 83 degrees and the average as 71 degrees.

![december_stats](https://user-images.githubusercontent.com/94208810/149611203-cd828cee-f830-4364-8e0f-d46c13b2a7e3.png)


## Deliverable 3 
## Summary
The analysis of the Oahu, Hawaii weather for both June and December provided W. Avy some solid statistical analysis—such as the mean, standard deviation, minimum, and maximum temperatures. The results were very similar for both June and December with only a small difference in temperature. The average temperature for both months were only 3 degrees different. It shows the consistency in weather throughout the year in Oahu. The analysis provided shows that a surf and shake shop business would be sustainable year round based on temperature.


![june_hist](https://user-images.githubusercontent.com/94208810/149611771-919b2346-67b4-4131-9798-d5084ce58bd7.png)



![dec_hist](https://user-images.githubusercontent.com/94208810/149611780-ce67c64c-ffea-41db-9f42-ef55cc319c41.png)
