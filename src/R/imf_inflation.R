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
  
  # Find African countries in the IFS database
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
    "CD", # Democratic Republic 