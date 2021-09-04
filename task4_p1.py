import pandas as pd
import os
import numpy as np

cwd = os.getcwd()
# Replace ProcessedTimeData.xlsx with input file name
data = cwd + r'\ProcessedTimeData.csv'

xl = pd.read_csv(data)

d = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'MinTT': [],
     'TT10': [], 'TT15': [], 'TT25': [], 'TT50': [], 'AvgTT': [], 'TT85': [], 'TT90': [], 'TT95': [],
     'MaxTT': [], 'StdDev': [], 'PT': [], 'PTI': [], 'BT': [], 'BTI': [], 'TTI': [],
     'L_Skew': [], 'L_Var': []}

d2 = {}

d3 = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [],
      'BT': [], 'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': [], 'AvgTT': []}

d4 = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [],
      'BT': [], 'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': [], 'AvgTT': []}

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
    PTI = PT/np.percentile(d2[x], 15)
    d['PTI'].append(round(PTI, 2))
    BT = PT - AVG
    d['BT'].append(round(BT, 2))
    BTI = BT/AVG
    d['BTI'].append(round(BTI, 2))
    TTI = AVG/np.percentile(d2[x], 15)
    d['TTI'].append(round(TTI, 2))
    if P50-P10 == 0:
        L_Skew = float('inf')
        d['L_Skew'].append(L_Skew)
    else:
        L_Skew = (P90 - P50) / (P50 - P10)
        d['L_Skew'].append(round(L_Skew, 2))
    L_Var = (P90 - P10)/P50
    d['L_Var'].append(round(L_Var, 2))

    if 2 < int(labels[2]) < 6:
        d3['LinkName'].append(labels[0])
        d3['Year'].append(labels[1])
        d3['Day-of-the-week'].append(labels[2])
        d3['Time-of-the-day'].append(labels[3])
        d3['PT'].append(round(PT, 2))
        d3['PTI'].append(round(PTI, 2))
        d3['BT'].append(round(BT, 2))
        d3['BTI'].append(round(BTI, 2))
        d3['TTI'].append(round(TTI, 2))
        d3['L_Skew'].append(round(L_Skew, 2))
        d3['L_Var'].append(round(L_Var, 2))
        d3['AvgTT'].append(round(AVG, 2))

    # Part 1 Weekends
    if int(labels[2]) == 1:
        d4['LinkName'].append(labels[0])
        d4['Year'].append(labels[1])
        d4['Day-of-the-week'].append(labels[2])
        d4['Time-of-the-day'].append(labels[3])
        d4['PT'].append(round(PT, 2))
        d4['PTI'].append(round(PTI, 2))
        d4['BT'].append(round(BT, 2))
        d4['BTI'].append(round(BTI, 2))
        d4['TTI'].append(round(TTI, 2))
        d4['L_Skew'].append(round(L_Skew, 2))
        d4['L_Var'].append(round(L_Var, 2))
        d4['AvgTT'].append(round(AVG, 2))

frame = pd.DataFrame(d3)
# Replace ProcessedTask4_Weekdays.csv with output file name
frame.to_csv("ProcessedTask4_Weekdays.csv", index=False)

frame2 = pd.DataFrame(d4)
# Replace ProcessedTask4_Weekends.csv with output file name
frame2.to_csv("ProcessedTask4_Weekends.csv", index=False)
