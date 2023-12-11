import numpy as np
import pandas as pd
import os
from sklearn.model_selection import TimeSeriesSplit

# Acquire Functions

# Before running the function, download the dataset from the link below and name it coffee_shop_sales.csv
# https://www.kaggle.com/code/ahmedabbas757/coffee-shop-sales
def get_coffee():
    """
    This function opens a locally stored .csv file containing the coffee shop sales data downloaded from 
    kaggle.com and displays it in a pandas dataframe.
    """
    filename = "coffee_shop_sales.csv"

    if os.path.isfile(filename):

        return pd.read_csv(filename)
    

# Prepare Functions

def set_index(df):
    """
    This function combines the date and time features from a pandas dataframe containing the coffee shop 
    sales data into a single feature, and then reset the dataframe index to the new date/time feature.
    """
    df['transaction_date_time'] = df['transaction_date'] + ' ' + df['transaction_time']
    df['transaction_date_time'] = pd.to_datetime(df['transaction_date_time'], format='%m/%d/%y %H:%M:%S')
    df = df.set_index('transaction_date_time')
    return df


def prep_coffee(df):  
    """
    This function creates new features from a pandas dataframe containing the coffee shop sales data, 
    removes transactions that exceed $20 from the dataset, and drops columns that will not be used for
    data exploration and modeling.
    """
# add columns
    df['transaction_total'] = df.transaction_qty * df.unit_price
    df['month']= df.index.month_name()
    df['day']= df.index.day_name()
    df['hour']= df.index.hour
# delete columns
    df = df.drop(columns=['transaction_id', 'transaction_date', 'transaction_time'])
# remove upper outliers
    df = df[df.transaction_total < 20]
    return df