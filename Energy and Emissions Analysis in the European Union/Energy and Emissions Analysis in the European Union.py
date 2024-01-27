import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Energy Consumption
df = pd.read_csv('/Users/gyeomi/Downloads/Statistical Review of World Energy Data.csv')
df
europe_data = df[df['Country'].str.contains('Total Europe')]

europe_data.head()

x_data = europe_data.loc[:, '1982':'2022']
x_data

x_data = x_data.T.reset_index()
x_data.columns = ['Year', 'Value']
x_data['Year'] = x_data['Year'].astype(float)
x_data['Value'] = x_data['Value'].astype(float)

plt.figure(figsize=(12, 6))
plt.plot(x_data['Year'], x_data['Value'], marker='o', linestyle='-')
plt.title('Energy Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Exajoules)')
plt.grid(True)
plt.show()


#Carbon Dioxide Emissions from Energy

carbon_df = pd.read_csv('/Users/gyeomi/Downloads/Carbon Dioxide Emissions from Energy.csv')
carbon_df
carbon_europe_data = carbon_df[carbon_df['Million tonnes of carbon dioxide'].str.contains('Total Europe')]
carbon_europe_data

x_car_data = carbon_europe_data.loc[:, '1982':'2022']
x_car_data = x_car_data.T.reset_index()
x_car_data.columns = ['Year', 'Value']
x_car_data
x_car_data['Year'] = x_car_data['Year'].astype(float)
x_car_data['Value'] = x_car_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_car_data['Year'], x_car_data['Value'], marker='o', linestyle='-')
plt.title('Carbon dioxide by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Million tonnes of carbon dioxide')
plt.grid(True)
plt.show()

# Oil consumption
oil_df= pd.read_csv('/Users/gyeomi/Downloads/Oil Consumption.csv')
oil_df
oil_eu_df = oil_df[oil_df['Exajoules'].str.contains('Total Europe')]
oil_eu_df

x_oil_data = oil_eu_df.loc[:, '1982':'2022']
x_oil_data = x_oil_data.T.reset_index()
x_oil_data.columns = ['Year', 'Value']
x_oil_data
x_oil_data['Year'] = x_oil_data['Year'].astype(float)
x_oil_data['Value'] = x_oil_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_oil_data['Year'], x_oil_data['Value'], marker='o', linestyle='-')
plt.title('Oil Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Oil Consumption (Exajoules)')
plt.grid(True)
plt.show()

#Coal consumprion
coal_df= pd.read_csv('/Users/gyeomi/Downloads/Coal_consumption.csv')
coal_df
coal_eu_df = coal_df[coal_df['Exajoules'].str.contains('Total Europe')]
coal_eu_df

x_coal_data = coal_eu_df.loc[:, '1982':'2022']
x_coal_data = x_coal_data.T.reset_index()
x_coal_data.columns = ['Year', 'Value']
x_coal_data
x_coal_data['Year'] = x_coal_data['Year'].astype(float)
x_coal_data['Value'] = x_coal_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_coal_data['Year'], x_coal_data['Value'], marker='o', linestyle='-')
plt.title('Coal Consumption by Year for European Countries (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Coal Consumption (Exajoules)')
plt.grid(True)
plt.show()

#Gas
gas_df= pd.read_csv('/Users/gyeomi/Downloads/gas_consumprion.csv')
gas_df
gas_eu_df = gas_df[gas_df['Exajoules'].str.contains('Total Europe')]
gas_eu_df

x_gas_data = gas_eu_df.loc[:, '1982':'2022']
x_gas_data = x_gas_data.T.reset_index()
x_gas_data.columns = ['Year', 'Value']
x_gas_data
x_gas_data['Year'] = x_gas_data['Year'].astype(float)
x_gas_data['Value'] = x_gas_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_gas_data['Year'], x_gas_data['Value'], marker='o', linestyle='-')
plt.title('Gas Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Gas Consumption (Exajoules)')
plt.grid(True)
plt.show()

#nuclear
nuclear_df= pd.read_csv('/Users/gyeomi/Downloads/nuclear_consumption.csv')
nuclear_df
nuclear_eu_df = nuclear_df[nuclear_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
nuclear_eu_df

x_nuclear_data = nuclear_eu_df.loc[:, '1982':'2022']
x_nuclear_data = x_nuclear_data.T.reset_index()
x_nuclear_data.columns = ['Year', 'Value']
x_nuclear_data
x_nuclear_data['Year'] = x_nuclear_data['Year'].astype(float)
x_nuclear_data['Value'] = x_nuclear_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_nuclear_data['Year'], x_nuclear_data['Value'], marker='o', linestyle='-')
plt.title('Nuclear Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Nuclear Consumption (Exajoules)')
plt.grid(True)
plt.show()

#renewable
renewable_df= pd.read_csv('/Users/gyeomi/Downloads/renewable_consumptiopn.csv')
renewable_df
renewable_eu_df = renewable_df[renewable_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
renewable_eu_df

x_renewable_data = renewable_eu_df.loc[:, '1982':'2022']
x_renewable_data = x_renewable_data.T.reset_index()
x_renewable_data.columns = ['Year', 'Value']
x_renewable_data
x_renewable_data['Year'] = x_renewable_data['Year'].astype(float)
x_renewable_data['Value'] = x_renewable_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_renewable_data['Year'], x_renewable_data['Value'], marker='o', linestyle='-')
plt.title('Renewable Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Renewable Consumption (Exajoules)')
plt.grid(True)
plt.show()


#solar
solar_df= pd.read_csv('/Users/gyeomi/Downloads/solar.csv')
solar_df
solar_eu_df = solar_df[solar_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
solar_eu_df

x_solar_data = solar_eu_df.loc[:, '1982':'2022']
x_solar_data = x_solar_data.T.reset_index()
x_solar_data.columns = ['Year', 'Value']
x_solar_data['Value'] = x_solar_data['Value'].str.replace('-','0')
x_solar_data['Value'] = x_solar_data['Value'].str.replace('^','0')
x_solar_data['Year'] = x_solar_data['Year'].astype(float)
x_solar_data['Value'] = x_solar_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_solar_data['Year'], x_solar_data['Value'], marker='o', linestyle='-')
plt.title('Solar Energy Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Solar Energy Consumption (Exajoules)')
plt.grid(True)
plt.show()

#wind
wind_df= pd.read_csv('/Users/gyeomi/Downloads/wind.csv')
wind_df
wind_eu_df = wind_df[wind_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
wind_eu_df

x_wind_data = wind_eu_df.loc[:, '1982':'2022']
x_wind_data = x_wind_data.T.reset_index()
x_wind_data.columns = ['Year', 'Value']
x_wind_data['Value'] = x_wind_data['Value'].str.replace('-','0')
x_wind_data['Value'] = x_wind_data['Value'].str.replace('^','0')
x_wind_data['Year'] = x_wind_data['Year'].astype(float)
x_wind_data['Value'] = x_wind_data['Value'].astype(float)


plt.figure(figsize=(12, 6))
plt.plot(x_wind_data['Year'], x_wind_data['Value'], marker='o', linestyle='-')
plt.title('Wind Energy Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Wind Energy Consumption (Exajoules)')
plt.grid(True)
plt.show()

#

import pandas as pd
import matplotlib.pyplot as plt

# Renewable Consumption Data
renewable_df = pd.read_csv('/Users/gyeomi/Downloads/renewable_consumptiopn.csv')
renewable_eu_df = renewable_df[renewable_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
x_renewable_data = renewable_eu_df.loc[:, '1982':'2022']
x_renewable_data = x_renewable_data.T.reset_index()
x_renewable_data.columns = ['Year', 'Renewable Consumption (Exajoules)']
x_renewable_data['Year'] = x_renewable_data['Year'].astype(float)
x_renewable_data['Renewable Consumption (Exajoules)'] = x_renewable_data['Renewable Consumption (Exajoules)'].astype(float)

# Solar Consumption Data
solar_df = pd.read_csv('/Users/gyeomi/Downloads/solar.csv')
solar_eu_df = solar_df[solar_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
x_solar_data = solar_eu_df.loc[:, '1982':'2022']
x_solar_data = x_solar_data.T.reset_index()
x_solar_data.columns = ['Year', 'Solar Consumption (Exajoules)']
x_solar_data['Year'] = x_solar_data['Year'].astype(float)
x_solar_data['Solar Consumption (Exajoules)'] = x_solar_data['Solar Consumption (Exajoules)'].str.replace('-', '0')
x_solar_data['Solar Consumption (Exajoules)'] = x_solar_data['Solar Consumption (Exajoules)'].str.replace('^', '0').astype(float)

# Wind Consumption Data
wind_df = pd.read_csv('/Users/gyeomi/Downloads/wind.csv')
wind_eu_df = wind_df[wind_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
x_wind_data = wind_eu_df.loc[:, '1982':'2022']
x_wind_data = x_wind_data.T.reset_index()
x_wind_data.columns = ['Year', 'Wind Consumption (Exajoules)']
x_wind_data['Year'] = x_wind_data['Year'].astype(float)
x_wind_data['Wind Consumption (Exajoules)'] = x_wind_data['Wind Consumption (Exajoules)'].str.replace('-', '0')
x_wind_data['Wind Consumption (Exajoules)'] = x_wind_data['Wind Consumption (Exajoules)'].str.replace('^', '0').astype(float)

# Other Consumption Data
other_df = pd.read_csv('/Users/gyeomi/Downloads/geothermal_biomass_other.csv')
other_eu_df = other_df[other_df['Exajoules (input-equivalent)'].str.contains('Total Europe')]
x_other_data = other_eu_df.loc[:, '1982':'2022']
x_other_data = x_other_data.T.reset_index()
x_other_data.columns = ['Year', 'geothermal_biomass_other Consumption (Exajoules)']
x_other_data['Year'] = x_other_data['Year'].astype(float)
x_other_data['geothermal_biomass_other Consumption (Exajoules)'] = x_other_data['geothermal_biomass_other Consumption (Exajoules)'].str.replace('-', '0')
x_other_data['geothermal_biomass_other Consumption (Exajoules)'] = x_other_data['geothermal_biomass_other Consumption (Exajoules)'].str.replace('^', '0').astype(float)

# Each energy type in 2022
solar_2022 = x_solar_data[x_solar_data['Year'] == 2022]['Solar Consumption (Exajoules)'].values[0]
wind_2022 = x_wind_data[x_wind_data['Year'] == 2022]['Wind Consumption (Exajoules)'].values[0]
other_2022 = x_other_data[x_other_data['Year'] == 2022]['geothermal_biomass_other Consumption (Exajoules)'].values[0]

# Each renewable energy type in 2022
renewable_2022 = x_renewable_data[x_renewable_data['Year'] == 2022]['Renewable Consumption (Exajoules)'].values[0]

# Renewable energy ratio from energy
solar_ratio = solar_2022 / renewable_2022
wind_ratio = wind_2022 / renewable_2022
other_ratio = other_2022 / renewable_2022

print(f'Solar Ratio: {solar_ratio:.2%}')
print(f'Wind Ratio: {wind_ratio:.2%}')
print(f'Other Ratio: {other_ratio:.2%}')

# Graph
plt.figure(figsize=(12, 6))

# Renewable Consumption 
plt.plot(x_renewable_data['Year'], x_renewable_data['Renewable Consumption (Exajoules)'], label='Renewable', marker='o', linestyle='-')

# Solar Consumption
plt.plot(x_solar_data['Year'], x_solar_data['Solar Consumption (Exajoules)'], label='Solar', marker='o', linestyle='-')

# Wind Consumption
plt.plot(x_wind_data['Year'], x_wind_data['Wind Consumption (Exajoules)'], label='Wind', marker='o', linestyle='-')

# geothermal_biomass_other
plt.plot(x_other_data['Year'], x_other_data['geothermal_biomass_other Consumption (Exajoules)'], label='Geothermal & Biomass & Other', marker='o', linestyle='-')

plt.title('Renewable Energy Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Exajoules)')
plt.grid(True)
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(12, 6))

# Renewable Consumption 
plt.bar(x_renewable_data['Year'], x_renewable_data['Renewable Consumption (Exajoules)'], label='Renewable', alpha=0.7)

# Solar Consumption 
plt.bar(x_solar_data['Year'], x_solar_data['Solar Consumption (Exajoules)'], label='Solar', alpha=1, color = 'red')

# Wind Consumption 
plt.bar(x_wind_data['Year'], x_wind_data['Wind Consumption (Exajoules)'], label='Wind', alpha=0.7)

# geothermal_biomass_other 
plt.bar(x_other_data['Year'], x_other_data['geothermal_biomass_other Consumption (Exajoules)'], label='Geothermal & Biomass & Other', alpha=0.5, color = 'purple')

plt.title('Renewable Energy Consumption by Year for EU (From 1982 to 2022)')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Exajoules)')
plt.grid(True)
plt.legend()
plt.show()



# Graph for Energy Resources
plt.figure(figsize=(12, 6))

# Renewable Consumption 
plt.plot(x_renewable_data['Year'], x_renewable_data['Renewable Consumption (Exajoules)'], label='Renewable', marker='o', linestyle='-')

# Nuclear Consumption 
plt.plot(x_nuclear_data['Year'], x_nuclear_data['Value'], label='Nuclear', marker='o', linestyle='-')

# Gas Consumption 
plt.plot(x_gas_data['Year'], x_gas_data['Value'], label='Gas', marker='o', linestyle='-')

# Coal Consumption 
plt.plot(x_coal_data['Year'], x_coal_data['Value'], label='Coal', marker='o', linestyle='-')

# Oil Consumption
plt.plot(x_oil_data['Year'], x_oil_data['Value'], label='Oil', marker='o', linestyle='-')

# Total
plt.plot(x_data['Year'], x_data['Value'], marker="D", linestyle='-')

plt.title('Energy Consumption by Year for European Countries')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Exajoules)')
plt.grid(True)
plt.legend()
plt.show()




# Carbon dioxiden data
carbon_df = pd.read_csv('/Users/gyeomi/Downloads/Carbon Dioxide Emissions from Energy.csv')
carbon_europe_data = carbon_df[carbon_df['Million tonnes of carbon dioxide'].str.contains('Total Europe')]
x_car_data = carbon_europe_data.loc[:, '1982':'2022']
x_car_data = x_car_data.T.reset_index()
x_car_data.columns = ['Year', 'Million tonnes of carbon dioxide']
x_car_data['Year'] = x_car_data['Year'].astype(float)
x_car_data['Million tonnes of carbon dioxide'] = x_car_data['Million tonnes of carbon dioxide'].astype(float)

# Graph
plt.figure(figsize=(12, 6))

# Renewable Consumption graph
plt.plot(x_renewable_data['Year'], x_renewable_data['Renewable Consumption (Exajoules)'], label='Renewable' , marker="*", linestyle='-',color='blue')
# Nuclear Consumption 
plt.plot(x_nuclear_data['Year'], x_nuclear_data['Value'], label='Nuclear', marker=4, linestyle='-', color='grey')
# Gas Consumption 
plt.plot(x_gas_data['Year'], x_gas_data['Value'], label='Gas', marker=5, linestyle='-',color='grey')
# Coal Consumption 
plt.plot(x_coal_data['Year'], x_coal_data['Value'], label='Coal', marker=6, linestyle='-',color='grey')
# Oil Consumption
plt.plot(x_oil_data['Year'], x_oil_data['Value'], label='Oil', marker=7, linestyle='-',color='grey')
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Exajoules)')
plt.grid(True)
plt.legend(loc='upper left')


# Carbon dioxiden graph 
ax2 = plt.twinx()
ax2.plot(x_car_data['Year'], x_car_data['Million tonnes of carbon dioxide'], label='Carbon Dioxide Emissions', marker="D", linestyle='-', color='red')
ax2.set_ylabel('Million tonnes of carbon dioxide')
ax2.legend(loc='upper right')

plt.title('Energy Consumption and Carbon Dioxide Emissions by Year for EU (From 1982 to 2022)')
plt.show()

# Renewable energy Consumption and Total energy Consumption in 1982 and 2022
renewable_1982 = x_renewable_data[x_renewable_data['Year'] == 1982]['Renewable Consumption (Exajoules)'].values[0]
renewable_2022 = x_renewable_data[x_renewable_data['Year'] == 2022]['Renewable Consumption (Exajoules)'].values[0]
total_1982 = x_data[x_data['Year'] == 1982]['Value'].values[0]
total_2022 = x_data[x_data['Year'] == 2022]['Value'].values[0]

# Renewable energy ratios in 1982 and 2022
percent_1982 = (renewable_1982 / total_1982) * 100
percent_2022 = (renewable_2022 / total_2022) * 100


# Piechart
labels = ['Renewable Energy', 'Other Energy']
sizes_1 = [percent_1982, 100 - percent_1982]  # 1982년의 renewable과 나머지 비율
sizes_2 = [percent_2022, 100 - percent_2022]  # 2022년의 renewable과 나머지 비율
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # 파이 조각을 분리

# Sub plot
plt.figure(figsize=(12, 6))

# First piechart
plt.subplot(1, 2, 1)
plt.pie(sizes_1, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Renewable Energy Consumption Ratio in EU in 1982')
plt.axis('equal')  # keep the shape df the circle

# Second piechart
plt.subplot(1, 2, 2)
plt.pie(sizes_2, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Renewable Energy Consumption Ratio in EU in 2022')
plt.axis('equal')  # keep the shape df the circle

plt.legend(labels, title = 'Energy Resources', loc='lower right')

# Two pie chart's distance
plt.subplots_adjust(wspace=0.5)

# 
plt.tight_layout()  # Subplot distance
plt.show()

# coal
x_coal_data
x_coal_data['Year'] = x_coal_data['Year'].astype(float)
x_coal_data['Value'] = x_coal_data['Value'].astype(float)
coal_1982 = x_coal_data[x_coal_data['Year'] == 1982]['Value'].values[0]
coal_2022 = x_coal_data[x_coal_data['Year'] == 2022]['Value'].values[0]

# gas
x_gas_data
x_gas_data['Year'] = x_gas_data['Year'].astype(float)
x_gas_data['Value'] = x_gas_data['Value'].astype(float)
gas_1982 = x_gas_data[x_gas_data['Year'] == 1982]['Value'].values[0]
gas_2022 = x_gas_data[x_gas_data['Year'] == 2022]['Value'].values[0]

# nuclear
x_nuclear_data
x_nuclear_data['Year'] = x_nuclear_data['Year'].astype(float)
x_nuclear_data['Value'] = x_nuclear_data['Value'].astype(float)
nuclear_1982 = x_nuclear_data[x_nuclear_data['Year'] == 1982]['Value'].values[0]
nuclear_2022 = x_nuclear_data[x_nuclear_data['Year'] == 2022]['Value'].values[0]

# oil 
x_oil_data
x_oil_data['Year'] = x_oil_data['Year'].astype(float)
x_oil_data['Value'] = x_oil_data['Value'].astype(float)
oil_1982 = x_oil_data[x_oil_data['Year'] == 1982]['Value'].values[0]
oil_2022 = x_oil_data[x_oil_data['Year'] == 2022]['Value'].values[0]

# Each energy ratio
renewable_percent_1982 = (renewable_1982 / total_1982) * 100
coal_percent_1982 = (coal_1982 / total_1982) * 100
gas_percent_1982 = (gas_1982 / total_1982) * 100
nuclear_percent_1982 = (nuclear_1982 / total_1982) * 100
oil_percent_1982 = (oil_1982 / total_1982) * 100

renewable_percent_2022 = (renewable_2022 / total_2022) * 100
coal_percent_2022 = (coal_2022 / total_2022) * 100
gas_percent_2022 = (gas_2022 / total_2022) * 100
nuclear_percent_2022 = (nuclear_2022 / total_2022) * 100
oil_percent_2022 = (oil_2022 / total_2022) * 100

# Piechart
labels = ['Renewable', 'Coal', 'Gas', 'Nuclear', 'Oil']
sizes_1 = [renewable_percent_1982, coal_percent_1982, gas_percent_1982, nuclear_percent_1982, oil_percent_1982]  # 1982년 비율
sizes_2 = [renewable_percent_2022, coal_percent_2022, gas_percent_2022, nuclear_percent_2022, oil_percent_2022]  # 2022년 비율
colors = ['lightcoral', 'lightblue', 'lightgreen', 'lightskyblue', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # 파이 조각을 분리

# Subplot
plt.figure(figsize=(12, 6))

# First pie
plt.subplot(1, 2, 1)
plt.pie(sizes_1, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Energy Consumption Ratio in EU in 1982')
plt.axis('equal')  # 원 모양 유지

# Second pie
plt.subplot(1, 2, 2)
plt.pie(sizes_2, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Energy Consumption Ratio in EU in 2022')
plt.axis('equal')  # 원 모양 유지

# distance between subplots
plt.subplots_adjust(wspace=0.5)

# Visualization
plt.tight_layout()  
plt.show()


