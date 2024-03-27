# Install and load required packages
if (!require(IMFData)) {
  devtools::install_github('mingjerli/IMFData')
}
library(IMFData)
library(tidyverse)

# Function to download inflation data for African countries
download_african_inflation_data <- function() {
  # Identify available datasets in IMF data
  availableDB <- DataflowMethod()
  
  # Assume "IFS" (International Financial Statistics) is the relevant dataset
  db_id <- "IFS"
  
  # Get dimension code of IFS dataset to search for the Consumer Price Index (CPI) as an indicator of inflation
  ifs_codes <- DataStructureMethod(db_id)
  indicator_code <- CodeSearch(ifs_codes, "CL_INDICATOR_IFS", "CPI")$CodeValue
  
  # List of African countries by two-digit country codes. Move into helpers later. 
  country_codes = c(
    "DZ", # Algeria
    "AO", # Angola
    "BJ", # Benin
    "BW", # Botswana
    "BF", # Burkina Faso
    "BI", # Burundi
    "CV", # Cabo Verde
    "CM", # Cameroon
    "CF", # Central African Republic
    "TD", # Chad
    "KM", # Comoros
    "CD", # Democratic Republic of the Congo
    "CG", # Republic of the Congo
    "CI", # Côte d'Ivoire
    "DJ", # Djibouti
    "EG", # Egypt
    "GQ", # Equatorial Guinea
    "ER", # Eritrea
    "SZ", # Eswatini
    "ET", # Ethiopia
    "GA", # Gabon
    "GM", # Gambia
    "GH", # Ghana
    "GN", # Guinea
    "GW", # Guinea-Bissau
    "KE", # Kenya
    "LS", # Lesotho
    "LR", # Liberia
    "LY", # Libya
    "MG", # Madagascar
    "MW", # Malawi
    "ML", # Mali
    "MR", # Mauritania
    "MU", # Mauritius
    "MA", # Morocco
    "MZ", # Mozambique
    "NA", # Namibia
    "NE", # Niger
    "NG", # Nigeria
    "RE", # Réunion
    "RW", # Rwanda
    "SH", # Saint Helena
    "ST", # Sao Tome and Principe
    "SN", # Senegal
    "SC", # Seychelles
    "SL", # Sierra Leone
    "SO", # Somalia
    "ZA", # South Africa
    "SS", # South Sudan
    "SD", # Sudan
    "TZ", # Tanzania
    "TG", # Togo
    "TN", # Tunisia
    "UG", # Uganda
    "EH", # Western Sahara
    "ZM", # Zambia
    "ZW"  # Zimbabwe
  )
  
  # Define a start and end date for the data query
  start_date <- "2000-01-01" # Modify as needed
  end_date <- "2023-01-01"   # Modify as needed
  
  # Download inflation data (CPI) for each African country with error handling
  inflation_data <- map_df(country_codes, function(country_code) {
    tryCatch({
      query_filter <- list(CL_FREQ = "A", CL_AREA_IFS = country_code, CL_INDICATOR_IFS = indicator_code)
      CompactDataMethod(db_id, query_filter, start_date, end_date, checkquery = FALSE, tidy = TRUE)
    }, error = function(e) {
      message(paste("Error in processing country code:", country_code, "Error:", e$message))
      return(NULL) # or an appropriate value or structure to signify an error
    })
  })
  
  # Return the data frame
  return(inflation_data)
}

# Calling the function to download the data
african_inflation_data <- download_african_inflation_data() %>%
  as_tibble() %>%
  janitor::clean_names() %>%
  mutate(obs_value = as.numeric(obs_value), time_period = as.factor(time_period))

result <- african_inflation_data %>%
  group_by(ref_area) %>%
  summarize(
    obs_value_diff = obs_value[which.max(as.numeric(time_period))] - obs_value[which.min(as.numeric(time_period))]
  )
