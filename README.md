**Project Description with Goals**
Coffee Shop Inc. wants to predict sales for its chain of three stores in New York City. With insights from analysis of transaction data--including times, dates and order details--we will construct a time-series model that accurately predicts future revenue.

**Project Planning**
-- acquire data from .csv file
-- write functions to acquire and prepare data in acquire.py file
-- split data into train and test sets
-- resample train data at various intervals (e.g. daily, weekly) and construct lag plots to look for temporal patterns
-- calculate RMSE on four models (two baseline and two non-baseline)
-- choose best-performing model (lowest RMSE)
-- apply best-performing model to test data
       
**Initial Hypothesis**
Coffee shop sales follow a temporal pattern that can be used to forecast future transaction totals. 

**Key Questions:**
-- Does time, day or month have an impact on transaction_total?
-- Which products are sold most in the morning hours? Which are sold most in the afternoon hours?  
-- Does each store location enjoy peak sales at the same times store_location matter?

**Data Dictionary**
|**Input Variables**|**Description**|
|-------------------|---------------|
| transaction_date | the date (month, day, year) of sale |
| transaction_time | the time (hour, minute, second) of sale |
| tranasction_date_time | feature that combines the transaction_date and transaction_time of each sale |
| transaction_qty | the amount of each item purchased |
| store_id | numerical identifier for the store where the sale occurred. There are three store ids (3, 5, 8) |
| store_location | location name of store where the sale occurred. There are three store locations (Astoria, Lower Manhattan, Hell's Kitchen. |
| product_id | numerical identifier of the product purchased. There are 80 unique product ids. |
| unit_price | the price paid for the product purchased, in U.S. dollars and cents. |
| product_category | there are nine product categories, Referred to as acidity or basicity. Wine has a lower pH (3.0-3.5) pH compared to water (7 pH). |
| product_type | Protects the wine against oxidation, which can effect the color and the taste of wine. |
| product_detail |  Standard measure of how much alcohol (ethanol) there is within a given volume of the drink, in percentage terms. |
| month | feature that isolates the month from January through June during which the sale occurred |
| day | feature that isolates the day of the week on which the sale occurred |
| hour | feature that isolates the hour between 7 a.m. (7) and 8 p.m. (20) during which the sale occurred |

**Instructions** 
-- download the coffee shop sales data from the link below and make sure it is saved as coffee_shop_sales.csv 
-- https://www.kaggle.com/code/ahmedabbas757/coffee-shop-sales
-- run get_coffee() function from acquire.py to open .csv file and display as a pandas dataframe
-- run set_index(df) function from acquire.py to combine the date and time features into a single column and reset the dataframe index to the new date/time feature
-- run the prep_coffee(df) function from acquire.py to add and delete columns (features) for exploration and modeling, and to remove outliers

**Key Findings** 
-- Patterns may be found in the time of day, weekday, or month that transactions occur.
-- Using Holt's Linear Trend and and changing the frequncy of data points (resampling) to daily is the best predictor of average transaction_total among the four models tested.

**Next Steps**
-- additional exploration to determine if product type or store location features can be used to forecast transaction_total
-- forecast transaction_total using Simple Average, Moving Average, Previous Cycle and Holt's Seasonal Trend to evaluate if model performance improves further

**Recommendations**
-- Use Holt's Linear Trend with resampling by day to forecast transaction totals.