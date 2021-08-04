import pandas as pd
import os
from datetime import timedelta
import numpy as np

cwd = os.getcwd()
data = cwd + r'\ProcessedTimeData.csv'

xl = pd.read_csv(data)

d = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'MinTT': [],
     'TT10': [], 'TT15': [], 'TT25': [], 'TT50': [], 'AvgTT': [], 'TT85': [], 'TT90': [], 'TT95': [],
     'MaxTT': [], 'StdDev': [], 'PT': [], 'PTI': [], 'BT': [], 'BTI': [], 'TTI': [],
     'L_Skew': [], 'L_Var': [], }

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
    d['MinTT'].append(round(np.min(d2[x]), 2))
    P10 = np.percentile(d2[x], 10)
    d['TT10'].append(round(P10, 2))
    d['TT15'].append(round(np.percentile(d2[x], 15), 2))
    d['TT25'].append(round(np.percentile(d2[x], 25), 2))
    P50 = np.percentile(d2[x], 50)
    d['TT50'].append(round(P50, 2))
    AVG = np.mean(d2[x])
    d['AvgTT'].append(round(AVG, 2))
    d['TT85'].append(round(np.percentile(d2[x], 85), 2))
    P90 = np.percentile(d2[x], 90)
    d['TT90'].append(round(P90, 2))
    d['TT95'].append(round(np.percentile(d2[x], 95), 2))
    d['MaxTT'].append(round(np.max(d2[x]), 2))
    d['StdDev'].append(round(np.std(d2[x]), 2))

    # Task 3 stuff
    PT = np.percentile(d2[x], 95)
    d['PT'].append(round(PT, 2))
    d['PTI'].append(round(PT/np.percentile(d2[x], 15), 2))
    BT = PT - AVG
    d['BT'].append(round(BT, 2))
    d['BTI'].append(round(BT/AVG, 2))
    d['TTI'].append(round(AVG/np.percentile(d2[x], 15), 2))
    if P50-P10 == 0:
        d['L_Skew'].append(float('inf'))
    else:
        d['L_Skew'].append(round((P90 - P50) / (P50 - P10), 2))
    d['L_Var'].append(round((P90 - P10)/P50, 2))

frame = pd.DataFrame(d)
frame.to_csv("ProcessedTask3.csv", index=False)
