import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 
from itertools import cycle, islice

flights = pd.read_csv('/Users/fantunez/Documents/dataMining/airline/airline_delay.csv') 
flights19 = flights.loc[flights['year'] == 2019]
flights20 = flights.loc[flights['year'] == 2020]

# total delay time in hours based on delay type for 2019
delay_type_19 = {
    'Weather Delay': [(flights19['weather_delay'].sum()) / 60],
    'National Aviation System': [(flights19['nas_delay'].sum()) / 60],
    'Security Delay': [(flights19['security_delay'].sum()) / 60],
    'Late Aircraft Dalay': [(flights19['late_aircraft_delay'].sum()) / 60]
}
# total delay time in hours based on delay type for 2020
delay_type_20 = {
    'Weather Delay': [(flights20['weather_delay'].sum()) / 60],
    'National Aviation System': [(flights20['nas_delay'].sum()) / 60],
    'Security Delay': [(flights20['security_delay'].sum()) / 60],
    'Late Aircraft Dalay': [(flights20['late_aircraft_delay'].sum()) / 60]
}

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5), sharex = True)

# Building the 2019 subplot
delay_type_19 = pd.DataFrame(data=delay_type_19)
my_colors_19 = list(islice(cycle(['deepskyblue', 'skyblue', 'steelblue', 'dodgerblue']), 4))
delay_type_19.plot(kind='barh', legend=True, color=my_colors_19, position = 0, ax = ax1)
ax1.set_title('Total Delay in Different Categories (2019)')
ax1.set_xlabel('Total Delay (hours)')
ax1.set_ylabel('Delay Category')


# building the 2020 subplot
delay_type_20 = pd.DataFrame(data=delay_type_20)
my_colors_20 = list(islice(cycle(['deepskyblue', 'skyblue', 'steelblue', 'dodgerblue']), 4))
delay_type_20.plot(kind='barh', legend=True, color=my_colors_20, position = 1, ax = ax2)
ax2.set_title('Total Delay in Different Categories (2020)')
ax2.set_xlabel('Total Delay (hours)')
ax2.set_ylabel('Delay Category')

plt.tight_layout()
plt.show()

# The total number of delays that were more than 15 min for each carrier
# this is not dependent on anything other than the carrier for 2019 and 2020
carrierDelay19 = flights19.groupby('carrier_name')['arr_del15'].sum()
carrierDelay20 = flights20.groupby('carrier_name')['arr_del15'].sum()

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 6), sharex=True)
plt.subplots_adjust(wspace=0.5)

# plotting 2019 and 2020
ax1.barh(carrierDelay19.index, carrierDelay19.values, color='skyblue')
ax1.set_title('Total Flights With Over 15min Delays (2019)')
ax1.set_ylabel('Airline')
ax2.barh(carrierDelay20.index, carrierDelay20.values, color='deepskyblue')
ax2.set_title('Total Flights With Over 15min Delays (2020)')
plt.tight_layout()
plt.show()

# Air delays due to air traffic per month
weatherCt19 = flights19.groupby('carrier_name')['nas_ct'].sum()
weatherTime19 = flights19.groupby('carrier_name')['nas_delay'].sum()

weatherCt20 = flights20.groupby('carrier_name')['nas_ct'].sum()
weatherTime20 = flights20.groupby('carrier_name')['nas_delay'].sum()

# Create subplots
fig, axs = plt.subplots(2, 2, figsize = (15, 6), sharey = True, sharex = True)
plt.subplots_adjust(wspace = 0.5, hspace = 0.5)

# plotting weather total and time total for 2019, this is the top row of plots
axs[0, 0].barh(weatherCt19.index, weatherCt19.values, color='skyblue')
axs[0, 0].set_title('Total Flights With NAS Delays (2019)')
axs[0, 0].set_ylabel('Airline')
axs[0, 0].set_xlabel('Total Flights Delayed')
axs[0, 1].barh(weatherTime19.index, (weatherTime19.values)/60, color='deepskyblue')
axs[0, 1].set_title('Total Time of NAS Delays (2020)')
axs[0, 1].set_xlabel('Total Delay (hours)')

# plotting weather total and time total for 2020, this is the bottom row of plots
axs[1, 0].barh(weatherCt20.index, weatherCt20.values, color='skyblue')
axs[1, 0].set_title('Total Flights With NAS Delays (2020)')
axs[1, 0].set_ylabel('Airline')
axs[1, 0].set_xlabel('Total Flights Delayed')
axs[1, 1].barh(weatherTime20.index, (weatherTime20.values)/60, color='deepskyblue')
axs[1, 1].set_title('Total Time of NAS Delays (2020)')
axs[1, 1].set_xlabel('Total Delay (hours)')
plt.tight_layout()
plt.show()