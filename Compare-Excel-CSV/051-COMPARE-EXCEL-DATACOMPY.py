import pandas as pd
# import numpy as np
import datacompy

df1=pd.read_excel('/home/chuck/Projects/jobian-ai/FakeHR/DATA/001_random_people.xlsx')
df2=pd.read_excel('/home/chuck/Projects/jobian-ai/FakeHR/DATA/002_random_people.xlsx')

compare = datacompy.Compare(
    df1,
    df2,
      
    # You can also specify a list
    # of columns
    join_columns = 'id', 
      
    # Optional, defaults to 0
    abs_tol = 0,
      
    # Optional, defaults to 0
    rel_tol = 0, 
      
    # Optional, defaults to 'df1'
    df1_name = 'Original',
      
    # Optional, defaults to 'df2'
    df2_name = 'New' 
    )
  
# if ignore_exra_columns=True, 
# the function won't return False
# in case of non-overlapping 
# column names
compare.matches(ignore_extra_columns = False) 

print(compare.report())