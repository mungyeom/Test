import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Open the Excel file and read its contents
file_path = '/Users/Desktop/Interview task.xlsx'

# Reading the Excel file into a pandas DataFrame
bags_on_belts_df = pd.read_excel(file_path, '2.1. Bags on the belt')
passengers_waiting_df = pd.read_excel(file_path, '2.2. Passengers waiting')

# Displaying the first few rows of each DataFrame to verify the contents
bags_on_belts_df.head(), passengers_waiting_df.head()

# Bags on the belt analyst

# Defining the capacity for each belt
belt_capacities = {'BELT 1': 160, 'BELT 2': 160, 'BELT 3': 160, 'BELT 4': 100}

# Modifying the code to consider the specific capacity of each belt
full_capacity_instances = bags_on_belts_df[bags_on_belts_df.apply(lambda row: row['Bags'] >= belt_capacities[row['Processor']], axis=1)]

# Displaying the corrected instances of full capacity
full_capacity_instances.head()

# Filtering the data to include only instances where the number of bags equals the belt's capacity
#full_capacity_instances = bags_on_belts_df[bags_on_belts_df['Bags'].isin(belt_capacities.values())]
#full_capacity_instances
# Finding the first instance (earliest time) each belt reached its full capacity
first_full_capacity_times = full_capacity_instances.groupby('Processor')['Time'].first()
	#aggregating and summarizing data. It allows you to group large amounts of data and compute operations on these groups
first_full_capacity_times

# Group by belt processor
grouped = full_capacity_instances.groupby('Processor')

# Retrieving the nth instance for each belt
second_full_capacity_times = grouped['Time'].nth(1)  # Second instance
third_full_capacity_times = grouped['Time'].nth(2)  # Third instance

second_full_capacity_times
third_full_capacity_times

# Creating a DataFrame to store instances of full capacity
full_capacity_all_instances = pd.DataFrame()

for belt, capacity in belt_capacities.items():
    # Filter for instances where the belt reached its full capacity
    full_capacity_belt = bags_on_belts_df[(bags_on_belts_df['Processor'] == belt) & (bags_on_belts_df['Bags'] == capacity)]
    full_capacity_all_instances = pd.concat([full_capacity_all_instances, full_capacity_belt]) 

#combine two or more data structures like DataFrames or Series

# Sorting by belt and time
full_capacity_all_instances = full_capacity_all_instances.sort_values(by=['Processor', 'Time'])

# Function to convert time to minutes past midnight
def time_to_minutes(time_val):
    return time_val.hour * 60 + time_val.minute + time_val.second / 60

# Applying the function to convert time to minutes past midnight
full_capacity_all_instances['Time in Minutes'] = full_capacity_all_instances['Time'].apply(time_to_minutes)

# Visualizing the times each belt reached full capacity in minutes past midnight
plt.figure(figsize=(12, 8))
for belt in belt_capacities.keys():
    # Extracting times for each belt
    times = full_capacity_all_instances[full_capacity_all_instances['Processor'] == belt]['Time in Minutes']
    
    # Plotting
    plt.plot(times, [belt] * len(times), 'o', label=belt)

plt.title('Instances of Full Capacity for Each Belt (in minutes past midnight)')
plt.xlabel('Time (minutes past midnight)')
plt.ylabel('Belt')
plt.xticks(range(0, 1441, 60), labels=[f'{h:02d}:00' for h in range(25)])  # Set x-axis labels as hours
plt.legend()
plt.grid(True)
plt.show()




# Group the data by belt and calculate the maximum number of bags for each belt
peak_bags_per_belt = bags_on_belts_df.groupby('Processor')['Bags'].max()

# The result is stored in peak_bags_per_belt
peak_bags_per_belt


# Calculating the peak number of bags for each belt
peak_bags_per_belt = bags_on_belts_df.groupby('Processor')['Bags'].max()

# Creating a bar chart to visualize the peak bag counts for each belt
plt.figure(figsize=(10, 6))
peak_bags_per_belt.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Peak Bag Counts on Each Belt')
plt.xlabel('Belt')
plt.ylabel('Number of Bags')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Function to calculate the difference in minutes between two time objects

def calculate_time_difference(start_time, end_time):
    # Calculate the difference in minutes
    start_minutes = start_time.hour * 60 + start_time.minute + start_time.second / 60
    end_minutes = end_time.hour * 60 + end_time.minute + end_time.second / 60

    # Calculate the difference
    difference = end_minutes - start_minutes
    return difference if difference >= 0 else difference + 24 * 60  # Adjust for midnight crossing

# Apply the function to the dataset
passengers_waiting_df['Waiting Time'] = passengers_waiting_df.apply(
    lambda row: calculate_time_difference(row['Start Time'], row['End Time']), axis=1)

# Checking the first few rows of the data with the calculated waiting time
passengers_waiting_df.head()

# Display the first few rows to verify the changes
passengers_waiting_df[['Start Time', 'End Time']].head()


# Applying the conversion to the DataFrame
passengers_waiting_df['Start Time Mins'] = passengers_waiting_df['Start Time'].apply(time_to_minutes)
passengers_waiting_df['End Time Mins'] = passengers_waiting_df['End Time'].apply(time_to_minutes)

passengers_waiting_df['End Time Mins']
passengers_waiting_df['Start Time Mins']
# Create a series to hold the passenger count for each minute of the day
minute_range = range(1440)  # 1440 minutes in a day
passenger_count_per_minute = pd.Series(index=minute_range, data=0)

for _, row in passengers_waiting_df.iterrows():
    passenger_count_per_minute[int(row['Start Time Mins']):int(row['End Time Mins'])] += 1

passenger_count_per_minute
# Find the maximum number of passengers at any given time
max_passengers = passenger_count_per_minute.max()
max_passengers

# Find the time corresponding to the maximum number of passengers
max_passengers_time = passenger_count_per_minute.idxmax()
max_passengers_time

plt.figure(figsize=(10, 6))
plt.scatter(passengers_waiting_df['Start Time Mins'], passengers_waiting_df['Waiting Time'], alpha=0.5)
plt.title('Scatter Plot of Passenger Waiting Times Throughout the Day')
plt.xlabel('Time of Day (minutes past midnight)')
plt.ylabel('Waiting Time (minutes)')
plt.show()

# Adding an arrow to the scatter plot at 731 minutes on the x-axis

plt.figure(figsize=(10, 6))
plt.scatter(passengers_waiting_df['Start Time Mins'], passengers_waiting_df['Waiting Time'], alpha=0.5)

# Add an arrow at x = 731 minutes
plt.annotate('Peak Time (731) - 12:11 AM, 396 passangers', xy=(731, 23), xytext=(731, 40),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

plt.title('Scatter Plot of Passenger Waiting Times Throughout the Day')
plt.xlabel('Time of Day (minutes past midnight)')
plt.ylabel('Waiting Time (minutes)')
plt.show()


# Plotting the distribution of waiting times
plt.figure(figsize=(10, 6))
plt.hist(passengers_waiting_df['Waiting Time'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Passenger Waiting Times')
plt.xlabel('Waiting Time (minutes)')
plt.ylabel('Number of Passengers')
plt.axvline(x=15, color='red', linestyle='--', label='IATA Standard (15 minutes)')
plt.legend()
plt.grid(True)
plt.show()

# Calculating the percentage of passengers who waited less than 15 minutes
percentage_within_standard = (passengers_waiting_df['Waiting Time'] < 15).mean() * 100
percentage_within_standard




