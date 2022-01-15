# Surfs_Up

## Analysis
### Overview
The following is Data Analysis for a business investor, W. Avy. The business venture is for a potential surf and shake shack to be located in Oahu, Hawaii. He would like to know if the surf and shake shop business would be sustainable year round.  
W. Avy gave me a weather database in SQLite. He specifically wants temperature data for the months of June and December in Oahu, in order to dermine 
First step in analysis was to retrieve the temperature data for month of June in Oahu. I did this with the sqlite database provided entitled "hawaii.sqlite". I used Python, Pandas funtions and methods, and SQLAlchemy to filter the date column of the Measurements table in "hawaii.sqlite" to retrieve all the temperatures for the month of June and December. I then converted those temperatures to a list and created two seperate DataFrames entitled june_df and dec_df from the two lists to generate the summary statistics. 

## Results

### Summary Statistics for the Month of June. 
  * The minimum temperature was 64 degrees
  * The maximum temperature was 85 degrees 
  * The average temperature as 74 degrees 

![june_stats (2)](https://user-images.githubusercontent.com/94208810/149614509-ffabca5b-0395-4078-9380-59aaffe4183d.png)

### Summary Statistics for the Month of December. 
  * The minimum temperature was 56 degrees.
  * The maximum temperature was 83 degrees. 
  * The average temperature as 71 degrees. 

![december_stats](https://user-images.githubusercontent.com/94208810/149614519-e628a70c-497b-4bae-8d46-9a74cb041e20.png)



## Deliverable 3 
## Summary
The analysis of the Oahu, Hawaii weather for both June and December provided W. Avy some solid statistical analysis—such as the mean, standard deviation, minimum, and maximum temperatures. The results were very similar for both June and December with only a small difference in temperature.  The average temperature for both months were only 3 degrees different. The precipitation for June and December are very low as well. I have added to histogram charts to show this data.It shows the consistency in weather throughout the year in Oahu. The analysis provided shows that a surf and shake shop business would be sustainable year round based on temperature.
Two additional queries to gather more weather data for June and December.

1. Query for june precipitation 
june_precip_results = session.query(Measurement.date, Measurement.prcp).filter(extract('month',Measurement.date)==6).all()

2. Query for December precipitation
dec_precip_results = session.query(Measurement.date, Measurement.prcp).filter(extract('month',Measurement.date)==12).all()

![june_hist](https://user-images.githubusercontent.com/94208810/149611771-919b2346-67b4-4131-9798-d5084ce58bd7.png)
![june_precip](https://user-images.githubusercontent.com/94208810/149613811-709d62db-f97a-46a7-b397-802e10c3a8d0.png)


![dec_hist](https://user-images.githubusercontent.com/94208810/149611780-ce67c64c-ffea-41db-9f42-ef55cc319c41.png)
![dec_precip](https://user-images.githubusercontent.com/94208810/149613810-aa9d1738-d1ea-4554-9dd5-4dd0897033b3.png)
