from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

df=pd.read_csv('data10.csv')
x=df['UTC_Time']
y=df['Speed']


fig, ax = plt.subplots(figsize=(10, 6))
plt.setp(ax.get_xticklabels(), rotation = 45)
speed_limit = int(input("Enter the Speed Limit of the Train: "))


# Line Graph
plt.plot(x,y, marker='o',markersize=5,linestyle='--',linewidth=2)
plt.plot(x,y, marker='o',markersize=4, markerfacecolor='black',linewidth=2 , color= "green",label='Safe')
plt.plot(x, y.where(y>speed_limit-10),color='orange',label="Warning")
plt.plot(x, y.where(y>speed_limit),color='r',label='Danger')



# # Bar Graph
plt.bar(x,y,color = "green")
plt.bar(x, y.where(y>speed_limit-5),color ='orange')
plt.bar(x, y.where(y>speed_limit),color ='r')


plt.title('Speed Monitoring for speedlimit '+str(speed_limit))
plt.xlabel('Time')
plt.ylabel('Speed')

plt.legend()

for i in range(len(y)):
    plt.text(i,y[i],y[i],ha = 'center')
plt.show()