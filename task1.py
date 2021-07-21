import pandas as pd
import os
from datetime import timedelta

cwd = os.getcwd()
data = cwd + r'\TravelTimeData.xlsx'

xl = pd.read_excel(data)

d = {'LinkName': [], 'Date': [], 'Year': [], 'Day-of-the-week': [], 'Time-of-the-day': [], 'Travel time': []}

for index, row in xl.iterrows():
    d['LinkName'].append(row['LinkName'])
    date = row['measurement_tstamp']
    d['Date'].append(date.strftime('%m/%d/%Y'))
    d['Year'].append(date.year)
    day = ((date.dayofweek + 1) % 7) + 1
    d['Day-of-the-week'].append(day)
    hour = date.strftime('%I:00 %p')
    nh = date + timedelta(hours=1)
    nextHour = nh.strftime('%I:00 %p')
    d['Time-of-the-day'].append(hour + '-' + nextHour)
    d['Travel time'].append(row['travel_time_minutes'])

frame = pd.DataFrame(d)
frame.to_csv("ProcessedTimeData.csv", index=False)
