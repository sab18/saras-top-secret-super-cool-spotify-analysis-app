import pandas as pd
# import plotly.graph_objs as go

import os, sys
src_dir_h1 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(src_dir_h1)

from data.master_df import df_cleaned

years = pd.to_datetime(df_cleaned['ts']).dt.year.unique()
# years_sorted=sorted(years)

years_sorted_all = sorted(years)

years_sorted=years_sorted_all.copy()
recent_year=2024
if recent_year in years_sorted:
    years_sorted.remove(recent_year)

# print(years_sorted)
# print(years_sorted_all)