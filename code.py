import numpy as np
import pandas as pd
import plotly.express as px
marksinp=[]
daysp=[]

df=pd.read_csv("Student Marks vs Days Present.csv")

marksinp=df["Marks In Percentage"].tolist()
daysp=df["Days Present"].tolist()

fig=px.scatter(x=daysp,y=marksinp)
fig.show()

correlation=np.corrcoef(df["Marks In Percentage"],df["Days Present"])
print(correlation[0,1])