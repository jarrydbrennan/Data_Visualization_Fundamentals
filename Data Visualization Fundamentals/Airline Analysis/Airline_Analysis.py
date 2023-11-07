import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
print("Min coach price: ",flight.coach_price.min())
print("Max coach price: ",flight.coach_price.max())
print("Average coach price: ",flight.coach_price.mean())
print("Median coach price: ", flight.coach_price.median())
plt.hist(flight['coach_price'])
plt.show()
plt.clf()
sns.boxplot(x='coach_price', data = flight)
plt.show()
plt.clf()
## Task 2
sns.boxplot(x=(flight.coach_price[flight.hours == 8]), data = flight)
plt.show()
plt.clf()
plt.hist((flight.coach_price[flight.hours == 8]))
plt.show()
plt.clf()
print("Min coach price for 8hr flight: ", min(flight.coach_price[flight.hours == 8]))
print("Max coach price for 8hr flight: ", max(flight.coach_price[flight.hours == 8]))
print("Average coach price for 8hr flight: ", (flight.coach_price[flight.hours == 8]).mean())
print("Median coach price for 8hr flight: ", (flight.coach_price[flight.hours == 8]).median())

## Task 3
sns.boxplot(x=(flight.delay[flight.delay <=300]), data = flight)
plt.show()
plt.clf()
sns.histplot(x=(flight.delay[flight.delay <=300]), data = flight)
plt.show()
plt.clf()
print("A typical flight delay: ", np.median(flight.delay))
## Task 4
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.lmplot(x = 'coach_price', y = 'firstclass_price', data = flight_sub, line_kws={'color':'black'}, lowess=True)
plt.show()
plt.clf()

## Task 5
sns.boxplot(x='inflight_meal', y='coach_price', data = flight, color='blue')
plt.show()
plt.clf()
sns.boxplot(x='inflight_entertainment', y='coach_price', data = flight, color = 'red')
plt.show()
plt.clf()
sns.boxplot(x='inflight_wifi', y='coach_price', data = flight, color ='orange')
plt.show()
plt.clf()
sns.histplot(flight, x = "coach_price", hue = flight.inflight_meal)
plt.show()
plt.clf()
sns.histplot(flight, x = "coach_price", hue = flight.inflight_entertainment)
plt.show()
plt.clf()
sns.histplot(flight, x = "coach_price", hue = flight.inflight_wifi)
plt.show()
plt.clf()
## Task 6
sns.lmplot(x = 'hours', y = 'passengers', x_jitter = .25, y_jitter = .25,scatter_kws={"s": 5, "alpha":0.2},fit_reg = False, data = flight_sub)
plt.show()
plt.clf()
## Task 7
perc = 0.05
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
sns.lmplot(x ='coach_price', y = 'firstclass_price', data = flight_sub,hue = 'day_of_week',scatter_kws={"s": 10, "alpha":0.5},fit_reg=False)
plt.show()
plt.clf()

## Task 8
sns.boxplot(x = 'day_of_week',y='coach_price', data = flight, hue ='redeye')
plt.show()
plt.clf()