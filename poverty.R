# Load necessary libraries
library(tidyr)
library(shiny)
library(dplyr)
library(ggplot2)
library(countrycode)

df_t <- data.frame(country = c("Afghanistan",
                             "Algeria",
                             "USA",
                             "France",
                             "New Zealand",
                             "Fantasyland"))

df_t %>% head()


# Read the CSV file
df <- 
  read.csv(file="data/API_SI.POV.LMIC_DS2_en_csv_v2_3545/API_SI.POV.LMIC_DS2_en_csv_v2_3545.csv", skip = 4, header = T) %>% 
  janitor::clean_names()

df %>% 
  head()

africa_pvrty_df <- 
  df %>% 
  select(-indicator_code) %>%
  filter(grepl("Sub-Saharan Africa", x=country_name)) %>% 
  gather(key = "year", value = "value", x1960:x2022) %>% 
  mutate(year = gsub(x = year, pattern = "x", replacement = "", ignore.case = TRUE)) %>%
  select(-x)


africa_pvrty_df %>% 
  filter(!is.na(value))

# Summarize missing values by column


df %>% 
  count(country_name)



data 
# Convert from long to wide format
wide_data <- data %>%
  pivot_wider(names_from = VariableCode, values_from = AggValue)
