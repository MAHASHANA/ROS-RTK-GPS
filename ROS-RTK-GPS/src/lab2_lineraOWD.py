import bagpy
from bagpy import bagreader
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import math

gps_owd= pd.read_csv('/home/ssrh98/eece5554/LAB2/src/bagfiles/Walking_Data_b/gps.csv')
 
gps_owd['UTM_northing_standard']= gps_owd['UTM_northing'] - gps_owd['UTM_northing'].min()
gps_owd['UTM_easting_standard']= gps_owd['UTM_easting'] - gps_owd['UTM_easting'].min()


x1 = gps_owd["UTM_northing_standard"]
y1 = gps_owd["UTM_easting_standard"]
x1 = gps_owd["UTM_northing_standard"].values[:,np.newaxis]
y1 = gps_owd["UTM_easting_standard"].values

x_values = x1[0:] - x1.min()
y_values = y1[0:] - y1.min()


#1st part
x_values_length = x_values[0:47]
y_values_length = y_values[0:47]

model = LinearRegression()
model.fit(x_values_length,y_values_length)

p_value = model.predict(x_values_length)
r_sq = model.score(x_values_length,y_values_length)
mse = mean_squared_error(y_values_length,p_value)
rmse = math.sqrt(mse)
print(rmse)
plt.xlabel('UTM northing')
plt.ylabel('UTM easting')
plt.scatter(x_values,y_values)
plt.plot(x_values_length,p_value)

#2nd part
x_values_breadth = x_values[42:58]
y_values_breadth = y_values[42:58]

model = LinearRegression()
model.fit(x_values_breadth,y_values_breadth)

p_value = model.predict(x_values_breadth)
r_sq = model.score(x_values_breadth,y_values_breadth)
mse = mean_squared_error(y_values_breadth,p_value)
rmse = math.sqrt(mse)
print(rmse)

plt.plot(x_values_breadth,p_value)

#3rd part
x_values_length1 = x_values[58:95]
y_values_length1 = y_values[58:95]

model = LinearRegression()
model.fit(x_values_length1,y_values_length1)

p_value = model.predict(x_values_length1)
r_sq = model.score(x_values_length1,y_values_length1)
mse = mean_squared_error(y_values_length1,p_value)
rmse = math.sqrt(mse)
print(rmse)
plt.scatter(x_values,y_values)
plt.plot(x_values_length1,p_value)


#2nd part
x_values_breadth = x_values[90:107]
y_values_breadth = y_values[90:107]

model = LinearRegression()
model.fit(x_values_breadth,y_values_breadth)

p_value = model.predict(x_values_breadth)
r_sq = model.score(x_values_breadth,y_values_breadth)
mse = mean_squared_error(y_values_breadth,p_value)
rmse = math.sqrt(mse)
print(rmse)

plt.plot(x_values_breadth,p_value)
plt.title("WALKING DATA In Noisy Environment")

plt.show()