import pandas as pd

# Load the dataset
file_path = '/Users/lnshuti/Desktop/portfolio/african-currencies/data/API_SI.POV.LMIC_DS2_en_csv_v2_3545/API_SI.POV.LMIC_DS2_en_csv_v2_3545.csv'
df = pd.read_csv(file_path, skiprows=4)

# Clean column names using a similar approach to janitor's clean_names in R
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '')

# Display the first few rows of the dataset
print(df.head())

# The unnamed_67 Column: All entries in the unnamed_67 column are missing. 

# Filtering the dataset for African countries
africa_pvrty_df = df[df['country_name'].str.contains("Sub-Saharan Africa")]

# Analyzing missing values by column in the filtered dataset
missing_values_summary = africa_pvrty_df.isnull().sum()

print(missing_values_summary)


# Remove the unnamed_67 column
africa_pvrty_df = africa_pvrty_df.drop(columns=['unnamed:_67'])

# Display the first few rows of the filtered dataset
print(africa_pvrty_df.tail())

# Convert from wide to long 
africa_pvrty_df = africa_pvrty_df.melt(id_vars=['country_name', 'country_code', 'indicator_name', 'indicator_code'], var_name='year', value_name='poverty_rate') 
africa_pvrty_df.head()