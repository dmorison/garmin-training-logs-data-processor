import pandas as pd
import numpy as np
import re

############################## functions

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

############################## swim

swim_df = pd.read_csv('./data_in/swim.csv')
print(swim_df.head())

swim_df = swim_df[:-1]

col_names = col_names_function(swim_df.columns)
swim_df.columns = col_names

swim_weeks = swim_df['time_period']
swim_df1 = swim_df[['total_activity_time', 'avg_time', 'max_time', 'average_pace']]
swim_df2 = swim_df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories']]

swim_df1 = swim_df1.applymap(times_function)
swim_df2 = swim_df2.applymap(other_function)

swim_df1a = pd.merge(swim_weeks, swim_df1, right_index=True, left_index=True)
swim_df2a = pd.merge(swim_weeks, swim_df2, right_index=True, left_index=True)
swim_df_complete = pd.merge(swim_df1a, swim_df2a, on='time_period')

print(swim_df_complete.head())
print(swim_df_complete.info())
swim_df_complete.to_csv('./data_out/swim.csv', encoding='utf-8', index=False)

############################## cycle

cycle_df = pd.read_csv('./data_in/cycle.csv')
print(cycle_df.head())

cycle_df = cycle_df[:-1]

col_names = col_names_function(cycle_df.columns)
cycle_df.columns = col_names

cycle_weeks = cycle_df['time_period']
cycle_df1 = cycle_df[['total_activity_time', 'avg_time', 'max_time']]
cycle_df2 = cycle_df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories', 'total_elev_gain', 'avg_elevation_gain', 'max_elevation_gain', 'average_heart_rate']]

cycle_df1 = cycle_df1.applymap(times_function)
cycle_df2 = cycle_df2.applymap(other_function)

cycle_df1a = pd.merge(cycle_weeks, cycle_df1, right_index=True, left_index=True)
cycle_df2a = pd.merge(cycle_weeks, cycle_df2, right_index=True, left_index=True)
cycle_df_complete = pd.merge(cycle_df1a, cycle_df2a, on='time_period')

print(cycle_df_complete.head())
print(cycle_df_complete.info())
cycle_df_complete.to_csv('./data_out/cycle.csv', encoding='utf-8', index=False)

############################## run

run_df = pd.read_csv('./data_in/run.csv')
print(run_df.head())

run_df = run_df[:-1]

col_names = col_names_function(run_df.columns)
run_df.columns = col_names
print(run_df.columns)

swim_weeks = run_df['time_period']
run_df1 = run_df[['total_activity_time', 'avg_time', 'max_time', 'average_pace']]
run_df2 = run_df[['activities', 'total_distance', 'average_distance', 'max_distance', 'activity_calories', 'total_elev_gain', 'avg_elevation_gain', 'max_elevation_gain', 'average_heart_rate']]

run_df1 = run_df1.applymap(times_function)
run_df2 = run_df2.applymap(other_function)

run_df1a = pd.merge(swim_weeks, run_df1, right_index=True, left_index=True)
run_df2a = pd.merge(swim_weeks, run_df2, right_index=True, left_index=True)
run_df_complete = pd.merge(run_df1a, run_df2a, on='time_period')

print(run_df_complete.head())
print(run_df_complete.info())
run_df_complete.to_csv('./data_out/run.csv', encoding='utf-8', index=False)

############################## strength

strength_df = pd.read_csv('./data_in/strength.csv')
print(strength_df.head())

strength_df = strength_df[:-1]

col_names = col_names_function(strength_df.columns)
strength_df.columns = col_names

swim_weeks = strength_df['time_period']
strength_df1 = strength_df[['total_activity_time', 'avg_time']]
strength_df2 = strength_df[['activities', 'activity_calories']]

strength_df1 = strength_df1.applymap(times_function)
strength_df2 = strength_df2.applymap(other_function)

strength_df1a = pd.merge(swim_weeks, strength_df1, right_index=True, left_index=True)
strength_df2a = pd.merge(swim_weeks, strength_df2, right_index=True, left_index=True)
strength_df_complete = pd.merge(strength_df1a, strength_df2a, on='time_period')

print(strength_df_complete.head())
print(strength_df_complete.info())
strength_df_complete.to_csv('./data_out/strength.csv', encoding='utf-8', index=False)