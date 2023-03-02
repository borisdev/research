Distance Per Dollar

You’re given a dataset of Uber rides with the traveling distance
("distance_to_travel") and cost ("monetary_cost") for each ride. For each date,
find the difference between the distance-per-dollar for that date and the
average distance-per-dollar for that year-month. Distance-per-dollar is defined
as the distance traveled divided by the cost of the ride.  


The output should
include the year-month (YYYY-MM) and the average difference in
distance-per-dollar for said year-month as an absolute value rounded to the 2nd
decimal. You should also count both success and failed request_status as the
distance and cost values are populated for all ride requests. Also, assume that
all dates are unique in the dataset. Order your results by the earliest request
date first. Source: stratascratch.com


Uber Rides

DIST COST     DATE
===================
10     100    Feb2
1      1      Feb2
2      1      Feb3
100    1000   Feb4

"for each date" --- so aggregate avg func group by date

- AVG(Dist/Cost) by day - month

DISTCOST     DATE  DAY MONTH
===============================
10          Feb2  Feb2 Feb
1           Feb2  Feb2 Feb
2           Feb3  Feb3 Feb 
.1          Feb4  Feb4 Feb

AVG by MONTH
================



- Dist per dollar month -- precalc this
- Dist per dollar day

YYYY-MM AVG_DIFF
-------------------------
