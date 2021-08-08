import pandas as pd
import os
from datetime import timedelta
import numpy as np

cwd = os.getcwd()
data = cwd + r'\ProcessedTask3.csv'

xl = pd.read_csv(data)

d = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [], 'BT': [],
     'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': []}

d2 = {'LinkName': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'PT': [], 'PTI': [], 'BT': [],
      'BTI': [], 'TTI': [], 'L_Skew': [], 'L_Var': []}

for index, row in xl.iterrows():
    # Part 1 Weekdays
    if 2 < row['Day-of-the-week'] < 6:
        d['LinkName'].append(row['LinkName'])
        d['Year'].append(row['Year'])
        d['Day-of-the-week'].append(row['Day-of-the-week'])
        d['Time-of-the-day'].append(row['Time-of-the-day'])
        d['PT'].append(row['PT'])
        d['PTI'].append(row['PTI'])
        d['BT'].append(row['BT'])
        d['BTI'].append(row['BTI'])
        d['TTI'].append(row['TTI'])
        d['L_Skew'].append(row['L_Skew'])
        d['L_Var'].append(row['L_Var'])

    # Part 1 Weekends
    if row['Day-of-the-week'] == 1:
        d2['LinkName'].append(row['LinkName'])
        d2['Year'].append(row['Year'])
        d2['Day-of-the-week'].append(row['Day-of-the-week'])
        d2['Time-of-the-day'].append(row['Time-of-the-day'])
        d2['PT'].append(row['PT'])
        d2['PTI'].append(row['PTI'])
        d2['BT'].append(row['BT'])
        d2['BTI'].append(row['BTI'])
        d2['TTI'].append(row['TTI'])
        d2['L_Skew'].append(row['L_Skew'])
        d2['L_Var'].append(row['L_Var'])

frame = pd.DataFrame(d)
frame.to_csv("ProcessedTask4_Weekdays.csv", index=False)

frame2 = pd.DataFrame(d2)
frame2.to_csv("ProcessedTask4_Weekends.csv", index=False)
