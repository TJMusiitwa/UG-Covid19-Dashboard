import io
from datetime import date, timedelta

import pandas as pd
import requests

file_date = date(2020, 3, 21)
dates = []

while file_date <= date.today():
    dates.append(file_date)
    file_date += timedelta(days=1)

files = []
for file in dates:
    file = file.strftime("%m-%d-%Y")
    print(file)
    url = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'.format(
        file)
    raw_string = requests.get(url).content
    df = pd.read_csv(io.StringIO(raw_string.decode('utf-8')))
    df['date'] = pd.to_datetime(file)
    df.rename(columns={'Country_Region': 'Country'}, inplace=True)
    files.append(df)

df = pd.concat(files, axis=0, ignore_index=True, sort=False)

df.drop(['Province/State', 'Province_State', 'Last Update', 'Last_Update',
         'FIPS', 'Admin2', 'Combined_Key', '404: Not Found', 'Lat', 'Long_', 'Latitude',
         'Longitude'], axis=1, inplace=True)

df_uganda = df[df['Country'] == 'Uganda']


df_uganda['Confirmed'] = df_uganda['Confirmed'].fillna(0).astype(int)
df_uganda['Deaths'] = df_uganda['Deaths'].fillna(0).astype(int)
df_uganda['Recovered'] = df_uganda['Recovered'].fillna(0).astype(int)
df_uganda['Active'] = df_uganda['Confirmed'] - \
    df_uganda['Deaths'] - df_uganda['Recovered']

df_uganda = df_uganda[['date',
                       'Country',
                       'Confirmed',
                       'Deaths',
                       'Recovered',
                       'Active',
                       ]]

ugandan_data = df_uganda.to_csv('uganda_data.csv', index=False)
