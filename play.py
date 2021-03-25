import pandas as pd
import numpy as np

data = {
  'apples': [3, 2, 0, 1], 
  'oranges': [0, 3, 7, 2],
  'bananas': [4, 9, 7, 0],
  'kiwis': [3, 2, 7, 5]
}

df = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
df = df.rename_axis('week')
print(df)

def other_func(x):
  if x < 3:
    return x
  else:
    return x * 10

# def times_function(x):
  # global other_func
  # return np.where(x < 3, x, other_func(x))

def test_func(x):
  result = x.apply(lambda x: other_func(x))
  return result
  # print(x)
  # x = x.tolist()
  # print(x)
  # for i in x:
  #   print(i)
  #   if i < 3:
  #     return i
  #   else:
  #     return i * 10

time_cols = ['oranges', 'kiwis']
df1 = df.apply(lambda x: test_func(x) if x.name in time_cols else x)
print(df1)