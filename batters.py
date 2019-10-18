import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    players_data = pandas.read_csv(filename)
    both = players_data.groupby('handedness').get_group('B')['avg'].tolist()
    righties = players_data.groupby('handedness').get_group('R')['avg'].tolist()
    lefties = players_data.groupby('handedness').get_group('L')['avg'].tolist()
    t_stat = scipy.stats.ttest_ind(lefties, righties, equal_var=False)

    return ((True, t_stat) if t_stat[1] > 0.95 else (False, t_stat))
