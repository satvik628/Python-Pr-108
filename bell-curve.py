# importing all modules required
import pandas as pd
import csv
import plotly.figure_factory as ff

# reading .csv file and storing in df
df=pd.read_csv("data/codeData.csv")

# plotting chart and generating output
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=False)
fig.show()

# run at terminal of vsc
