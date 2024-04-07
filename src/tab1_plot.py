import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


#import matplotlib.pyplot as plt

# import os,sys
# src_dir_h2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
# sys.path.append(src_dir_h2)

from master_df import df_cleaned
from unique_years_list import years_sorted


# print(df_cleaned.head())
# print(years_sorted)

year_list = []
mins_sum_list = []

for year in years_sorted:
    filtered_by_year = df_cleaned[pd.to_datetime(df_cleaned['ts']).dt.year == year]
    mins_sum_for_year = filtered_by_year['ms_played'].sum() / 1000 / 60

    year_list.append(year)
    mins_sum_list.append(mins_sum_for_year)

#print(mins_sum_list)

m,b = np.polyfit(year_list, mins_sum_list, 1)
y_pred=m*np.array(year_list)+b
r_squared = r2_score(mins_sum_list, y_pred)


raw_data_plotted = go.Scatter(x=year_list, y=mins_sum_list, mode='lines+markers', name='actual listening data')
fit_line = go.Scatter(x=year_list, y=y_pred, mode='lines', name=f'linear fit (R\u00b2={round(r_squared,2)})')


fig_mins_vs_year = go.Figure(data=[raw_data_plotted, fit_line])

fig_mins_vs_year.update_layout(
    xaxis_title='Year',
    yaxis_title='Minutes Listened',
    showlegend=True,
    legend=dict(
        x=0,    # Position the legend at x=1 (right)
        y=1,    # Position the legend at y=1 (top)
        traceorder='normal',  # Keep the order of legend entries as specified in the trace
    )
    #margin=dict(t=0)  # Show legend with original data and fit line
)
fig_mins_vs_year.update_layout(
    margin=dict(l=20, r=20, t=0, b=20),
)

year_total_music=round((525600-b)/m)