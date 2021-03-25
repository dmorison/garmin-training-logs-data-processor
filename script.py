import pandas as pd
import numpy as np
import re

def col_names_function(x):
  return x.str.lower().str.replace(' ', '_')

def other_function(x):
  if x == "--":
    return np.nan
  else:
    num = re.sub("[^\d\.]", "", str(x))
    return round(float(num), 1)

def times_function(x):
  if x == "--":
    return np.nan
  else:
    hms = x.split()[0]
    hms_arr = hms.split(":")
    seconds = int(hms_arr[len(hms_arr) - 1])
    minutes = 0
    hours = 0
    if len(hms_arr) > 2:
      hours = (int(hms_arr[0]) * 3600)
      minutes = (int(hms_arr[1]) * 60)
    else:
      minutes = int(hms_arr[0]) * 60
    return hours + minutes + seconds

def series_other_function(x):
  global other_function
  return x.apply(lambda y: other_function(y))

def series_time_function(x):
  global times_function
  return x.apply(lambda y: times_function(y))

def processDataFunction(sport):
  global col_names_function
  # global other_function
  # global times_function
  global series_other_function
  global series_time_function

  df = pd.read_csv('./data_in/' + sport + '.csv', index_col='Time Period', parse_dates=True)
  df = df.rename_axis('week')

  df = df[:-1]

  col_names = col_names_function(df.columns)
  df.columns = col_names

  print(df.head())
  
  time_df = None
  other_df = None
  if sport == "swim":
    time_df = df[['total_activity_time', 'avg_time', 'max_time', 'average_pace']]
    other_df = df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories']]
  elif sport == "cycle":
    time_df = df[['total_activity_time', 'avg_time', 'max_time']]
    other_df = df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories', 'total_elev_gain', 'avg_elevation_gain', 'max_elevation_gain', 'average_heart_rate']]
  elif sport == "run":
    time_df = df[['total_activity_time', 'avg_time', 'max_time', 'average_pace']]
    other_df = df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories', 'total_elev_gain', 'avg_elevation_gain', 'max_elevation_gain', 'average_heart_rate']]
  elif sport == "strength":
    time_df = df[['total_activity_time', 'avg_time']]
    other_df = df[['activities', 'activity_calories']]
  
  time_cols = ['total_activity_time', 'avg_time', 'max_time', 'average_pace']
  other_cols = ['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories', 'total_elev_gain', 'avg_elevation_gain', 'max_elevation_gain', 'average_heart_rate']
  result = df.apply(lambda x: series_time_function(x) if x.name in time_cols else series_other_function(x))

  if sport == "swim":
    result['average_pace'] = result['average_pace'].map(lambda x: x / 10)

  print(result.head())
  print("------------------")

  result.to_csv('./data_out/' + sport + '.csv', encoding='utf-8')

sports = ["swim", "cycle", "run", "strength"]
for sport in sports:
  processDataFunction(sport)
