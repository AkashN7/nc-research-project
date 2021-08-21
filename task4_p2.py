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
     'L_Skew': [], 'L_Var': [], }

d2 = {}

d3 = {'LinkName': [], 'Date': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [],
      'BT': [], 'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': []}

d4 = {'LinkName': [], 'Date': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [],
      'BT': [], 'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': []}

d5 = {'LinkName': [], 'Date': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [],
      'BT': [], 'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': []}

for index, row in xl.iterrows():
    name = str(row['LinkName']) + '#' + str(row['Year']) + '#' + str(row['Day-of-the-week']) +\
           '#' + str(row['Time-of-the-day']) + '#' + str(row['Date'])
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

    # Task 4 Part 2 Section 1
    if labels[4] == "03/12/2017" or labels[4] == "01/17/2018" or labels[4] == "04/02/2019" or labels[4] == "09/16/2018"\
            or labels[4] == "09/17/2018":
        d3['LinkName'].append(labels[0])
        d3['Date'].append(labels[4])
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

    elif 2 < int(labels[2]) < 6:
        d4['LinkName'].append(labels[0])
        d4['Date'].append(labels[4])
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

    elif int(labels[2]) == 1:
        d5['LinkName'].append(labels[0])
        d5['Date'].append(labels[4])
        d5['Year'].append(labels[1])
        d5['Day-of-the-week'].append(labels[2])
        d5['Time-of-the-day'].append(labels[3])
        d5['PT'].append(round(PT, 2))
        d5['PTI'].append(round(PTI, 2))
        d5['BT'].append(round(BT, 2))
        d5['BTI'].append(round(BTI, 2))
        d5['TTI'].append(round(TTI, 2))
        d5['L_Skew'].append(round(L_Skew, 2))
        d5['L_Var'].append(round(L_Var, 2))

# Processed data for selected dates
frame3 = pd.DataFrame(d3)
# Replace ProcessedTask4_SelectedDates.csv with output file name
frame3.to_csv("ProcessedTask4_SelectedDates.csv", index=False)

# Processed data for weekdays excluding selected dates
frame3 = pd.DataFrame(d4)
# Replace ProcessedTask4_SelectedDates_Weekdays.csv with output file name
frame3.to_csv("ProcessedTask4_SelectedDates_Weekdays.csv", index=False)

# Processed data for weekends excluding selected dates
frame3 = pd.DataFrame(d5)
# Replace ProcessedTask4_SelectedDates_Weekends.csv with output file name
frame3.to_csv("ProcessedTask4_SelectedDates_Weekends.csv", index=False)
