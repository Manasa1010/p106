import numpy as np
import pandas as pd
import plotly.express as px
coffeeInml=[]
sleepInHours=[]

df=pd.read_csv("cups of coffee vs hours of sleep.csv")

coffeeInml=df["Coffee in ml"].tolist()
sleepInHours=df["sleep in hours"].tolist()

fig=px.scatter(x=coffeeInml,y=sleepInHours)
fig.show()

correlation=np.corrcoef(df["Coffee in ml"],df["sleep in hours"])
print(correlation[0,1])