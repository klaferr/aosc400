# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 00:15:57 2018
turned on around 12:40pm, above eyelevel at 12:42pm. pulled down and relaunched around 12:48
if sampled every 30 seconds, 16 rows should be skipped

@author: Kris
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



#%%   
   
#import Axes3D
#read in aosc data
data1 = "LOG0001.csv"
tim1, tim2, time_1, temp_1, hum_1, pr_1, alt_1 = np.loadtxt(data1, delimiter=',', unpack = True, skiprows = 17) #, usecols=range(7))

#reed's group
time_4, temp_4, hum_4, pr_4, alt_4, light_4 = np.loadtxt('LOG00004.csv', delimiter=',', unpack = True, skiprows = 5)
time_5, temp_5, hum_5, pr_5, alt_5, light_5 = np.loadtxt("LOG00005.csv", delimiter=',', unpack = True, skiprows = 1)
time_6, temp_6, hum_6, pr_6, alt_6, light_6 = np.loadtxt('LOG00006.csv', delimiter=',', unpack = True, skiprows = 1)
time_7, temp_7, hum_7, pr_7, alt_7, light_7 = np.loadtxt("LOG0007.csv", delimiter=',', unpack = True, skiprows = 1)
time_8, temp_8, hum_8, pr_8, alt_8, light_8 = np.loadtxt('LOG00008.csv', delimiter=',', unpack = True, skiprows = 1)
time_9, temp_9, hum_9, pr_9, alt_9, light_9 = np.loadtxt("LOG00009.csv", delimiter=',', unpack = True, skiprows = 1)
time_10, temp_10, hum_10, pr_10, alt_10, light_10 = np.loadtxt('LOG00010.csv', delimiter=',', unpack = True, skiprows = 1)

#need to use values from launch date to make these absolute and not relative

#temp is 49 deg
#if 49 is 13 diff is 36


#%%
#can we take average of the values every 5 steps specifically altitude? theres a few values i think are outliers and false measurements
time = np.concatenate((time_4, time_5, time_6, time_7, time_8, time_9, time_10), axis = 0)
time = time/(60*1000)
temp = np.concatenate((temp_4,temp_5,temp_6,temp_7,temp_8,temp_9,temp_10), axis = 0)
hum = np.concatenate((hum_4,hum_5, hum_6, hum_7, hum_8, hum_9, hum_10), axis = 0)
pr = np.concatenate((pr_4,pr_5,pr_6,pr_7,pr_8,pr_9,pr_10), axis = 0)
alt = np.concatenate((alt_4,alt_5,alt_6,alt_7,alt_8,alt_9,alt_10), axis = 0)
#light = np.concatenate((temp_4,temp_5,temp_6,temp_7,temp_8,temp_9,temp_10), axis = 0)

temp = temp + 36;
temp_1 = temp_1 + 36;
#%%

plt.figure()
plt.scatter(time[::25], temp[::25])
plt.scatter(tim1[::10], temp_1[::10],  c='k', label = "our group")
plt.xlabel("time")
plt.ylabel("temp")

#%%
plt.figure()
plt.scatter(time[::25], hum[::25], cmap='viridis')
plt.scatter(tim1[::10], hum_1[::10], cmap = 'viridis', label = "our's group")
plt.xlabel("time")
plt.ylabel("humditiy")

plt.figure()
plt.scatter(time[::25], pr[::25], cmap='viridis')
#plt.scatter(time[::20], pr[::20], label = "reed's group")
plt.xlabel("time")
plt.ylabel("pressure")
plt.legend()

plt.figure()
plt.scatter(time[::25], alt[::25], cmap='viridis')
#plt.scatter(time_1[::10], alt_1[::10], label = "our group")
plt.xlabel("time")
plt.ylabel("alt")

plt.figure()
plt.scatter(temp[::25] , alt[::25], c = time[::25], cmap='viridis')
#plt.scatter(temp_1[::10] , alt_1[::10])
plt.xlabel("temp")
plt.ylabel("alt")
plt.colorbar()

plt.figure()
plt.scatter( temp[::25] , hum[::25], c = time[::25], cmap='viridis')
#plt.scatter( temp_1[::10] , hum_1[::10])
plt.xlabel("temp")
plt.ylabel("hum")
plt.colorbar()

plt.figure()
plt.scatter( temp[::25] , pr[::25], c=time[::25], cmap='viridis')
#plt.scatter( temp_1[::10] , pr_1[::10])
plt.xlabel("temp")
plt.ylabel("pressure")
plt.colorbar()

#%%
plt.figure()
ax = plt.axes(projection='3d')
#z = np.array([time, alt])
ax.scatter3D(temp[::25], pr[::25] , alt[::25], c = time[::25], cmap='viridis')
plt.xlabel("temp")
plt.ylabel("humidity")
#plt.colorbar()
#plt.zlabel("alt")



#wanna make more of these that show time as a color scale!!!
