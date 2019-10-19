import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms

    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
    '''
    
    column = turnstile_weather['ENTRIESn_hourly']
    plt.figure()
    column.loc[lambda column: column > 0].hist()
    column.loc[lambda column: column == 0].hist()
    #print(column.loc[lambda column: column > 0])
    return plt
