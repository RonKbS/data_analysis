from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # Two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Data in the csv file at the link below:
    # https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/hr_year.csv
    #
    # Ggplot at the following link:
    # https://github.com/yhat/ggplot/

    df = read_csv(hr_year_csv)
    gg = ggplot(df, aes(x='yearID', y='HR')) + geom_point(color='red') + geom_line(color='red')
    # + ggtitle('title') + xlab('x-lablel') + ylab('y-label')
    return gg
