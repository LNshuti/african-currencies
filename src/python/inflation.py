import pandas as pd
import matplotlib.pyplot as plt
import os
# Print current directory path
print(os.getcwd())


# Load the dataset, skipping the first two rows
file_path = './data/inflation/Country_Indexes_And_Weights.xlsx'
df = pd.read_excel(file_path, skiprows=2)

# Dropping columns from 1950M01 to 2014M1 as they are empty
columns_to_drop = [col for col in df.columns if 'M' in col and int(col.split('M')[0]) < 2014]
df = df.drop(columns=columns_to_drop)

# Reshaping the DataFrame for visualization
df_melted = df.melt(id_vars=["Unnamed: 0"], var_name="Date", value_name="Index")

print(df_melted.head())

# Separating 'Consumer Price Index, All items' from the components
cpi_all_items = df_melted[df_melted["Unnamed: 0"] == "Consumer Price Index, All items"]
components = df_melted[df_melted["Unnamed: 0"] != "Consumer Price Index, All items"]

cpi_all_items['InflationRate'] = cpi_all_items['Index'].pct_change() * 100
cpi_all_items['Date'] = pd.to_datetime(cpi_all_items['Date'], format='%YM%m')

print(components.head())

fig, ax1 = plt.subplots(figsize=(15, 6))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('CPI Index', color=color)
ax1.plot(cpi_all_items['Date'], cpi_all_items['Index'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Inflation Rate (%)', color=color)
ax2.plot(cpi_all_items['Date'], cpi_all_items['InflationRate'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()


# Plotting 'Consumer Price Index, All items'
plt.figure(figsize=(15, 6))
plt.plot(cpi_all_items['Date'], cpi_all_items['Index'], label='CPI All Items')
plt.title('Consumer Price Index, All items in Rwanda')
plt.xlabel('Date')
plt.ylabel('Index')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Plotting the components of inflation
# Using stacked bar chart if the components are suitable for such representation
unique_components = components["Country Series"].unique()

# Check if a stacked bar chart is appropriate (i.e., if components are part of a whole)
# For simplicity, assuming they are and proceeding with a stacked bar chart.
plt.figure(figsize=(15, 6))

bottom = None
for component in unique_components:
    component_data = components[components["Country Series"] == component]
    plt.bar(component_data['Date'], component_data['Index'], bottom=bottom, label=component)
    if bottom is None:
        bottom = component_data['Index']
    else:
        bottom += component_data['Index']

plt.title('Components of Inflation in Rwanda')
plt.xlabel('Date')
plt.ylabel('Index')
plt.xticks(rotation=45)
plt.legend()
plt.show()

