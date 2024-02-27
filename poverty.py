import pandas as pd

# Load the dataset
file_path = '/mnt/data/API_SI.POV.LMIC_DS2_en_csv_v2_3545.csv'
df = pd.read_csv(file_path, skiprows=4)

# Clean column names using a similar approach to janitor's clean_names in R
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '')

# Display the first few rows of the dataset
df.head()

# The unnamed_67 Column: All entries in the unnamed_67 column are missing. 

# Filtering the dataset for African countries
africa_pvrty_df = df[df['country_name'].str.contains("Africa")]

# Analyzing missing values by column in the filtered dataset
missing_values_summary = africa_pvrty_df.isnull().sum()

missing_values_summary
