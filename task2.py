import pandas as pd
import os
from datetime import timedelta
import numpy as np

cwd = os.getcwd()
data = cwd + r'\ProcessedTimeData.csv'

xl = pd.read_csv(data)

d = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'MinTT': [],
     'TT10': [], 'TT15': [], 'TT25': [], 'TT50': [], 'AvgTT': [], 'TT85': [], 'TT90': [], 'TT95': [],
     'MaxTT': [], 'StdDev': []}

# for i in range(1, 5):
#     ln = 'Link' + str(i)
#     for j in range(7, 10):
#         yr = '201' + str(j)
#         for k in range(1, 8):
#             for x in range(0, 24):
#                 arr = []
#                 if x != 23:
#                     time = str(x) + ':00-' + str(x+1) + ':00'
#                 elif x == 23:
#                     time = '23:00-0:00'
#                 while

d2 = {}

for index, row in xl.iterrows():
    name = str(row['LinkName']) + '#' + str(row['Year']) + '#' + str(row['Day-of-the-week']) +\
           '#' + str(row['Time-of-the-day'])
    if name in d2:
        d2[name].append(row['Travel time'])
    else:
        d2[name] = [row['Travel time']]

for x in d2:
    labels = x.split('#')
    d['LinkName'].append(labels[0])
    d['Year'].append(labels[1])
    d['Day-of-the-week'].append(labels[2])
    d['Time-of-the-day'].append(labels[3])
    d['MinTT'].append(np.min(d2[x]))
    d['TT10'].append(np.percentile(d2[x], 10))
    d['TT15'].append(np.percentile(d2[x], 15))
    d['TT25'].append(np.percentile(d2[x], 25))
    d['TT50'].append(np.percentile(d2[x], 50))
    d['AvgTT'].append(np.mean(d2[x]))
    d['TT85'].append(np.percentile(d2[x], 85))
    d['TT90'].append(np.percentile(d2[x], 90))
    d['TT95'].append(np.percentile(d2[x], 95))
    d['MaxTT'].append(np.max(d2[x]))
    d['StdDev'].append(np.std(d2[x]))

frame = pd.DataFrame(d)
frame.to_csv("ProcessedTask2.csv", index=False)
