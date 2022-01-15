# Surfs_Up

## Overview

The following is Data Analysis for a business investor, W. Avy. The business venture is for a potential surf and shake shack to be located in Oahu, Hawaii. He would like to know if the surf and shake shop business would be sustainable year round.  
W. Avy gave me a weather database in SQLite. He specifically wants temperature data for the months of June and December in Oahu, in order to dermine 
First step in analysis was to retrieve the temperature data for month of June in Oahu. I did this with the sqlite database provided entitled "hawaii.sqlite". I used Python, Pandas funtions and methods, and SQLAlchemy to filter the date column of the Measurements table in "hawaii.sqlite" to retrieve all the temperatures for the month of June and December. I then converted those temperatures to a list and created two seperate DataFrames entitled june_df and dec_df from the two lists to generate the summary statistics. 

## Deliverable 1
### Summary Statistics for the Month of June over 7 years from June 2010 to June 2017.
The month of June showed the minimum temperature was 64 degrees, maximum temperature was 85 and the average as 74. 
![Screenshot (4)](https://user-images.githubusercontent.com/94208810/149610732-7b7659b9-a259-46ee-8531-74b70a9fc735.png)

## Deliverable 2
### Summary Statistics for the Month of December over 7 years from December 2010 to December 2017. 
The Month of December showed the minimum temperature of 56 degrees, maximum temperature as 83 degrees and the average as 71 degrees.
![Screenshot (6)](https://user-images.githubusercontent.com/94208810/149610778-71c1712c-3688-4a47-81c3-2564b59400f3.png)


## Deliverable 3 
## Summary
The analysis of the Oahu, Hawaii weather for both June and December provided to W. Avy some solid statistical analysis—such as the mean, standard deviation, minimum, and maximum temperatures. The results were very similar for both June and December with only small difference in temperature degrees. The average temperature for both months were only 3 degrees different. It shows the consistency in weather throughout the year in Oahu. The analysis provided shows that a surf and shake shop business would be sustainable year round based on temperature.  
