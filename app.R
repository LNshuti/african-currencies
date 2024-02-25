# Load necessary libraries
library(tidyr)
library(shiny)
library(dplyr)
library(ggplot2)



# Read the CSV file
data <- read.csv("data/FebPwtExport2212024.csv")

# Convert from long to wide format
wide_data <- data %>%
  pivot_wider(names_from = VariableCode, values_from = AggValue)


# Step 4: Define UI
ui <- fluidPage(
  titlePanel("Currency Exchange Rate Comparison"),
  sidebarLayout(
    sidebarPanel(
      selectInput("country", "Select a Country:",
                  choices = unique(wide_data$RegionCode))
    ),
    mainPanel(
      plotOutput("exchange_rate_plot")
    )
  )
)

# Step 5: Define server logic
server <- function(input, output) {
  # Plot the data
  output$exchange_rate_plot <- renderPlot({
    country_data <- filter(wide_data, RegionCode == input$country)
    
    # Example plot (modify as needed)
    ggplot(country_data, aes(x = YearCode, y = xr)) + # Replace 'xr' with the appropriate variable column
      geom_line() +
      labs(title = paste("Historical Exchange Rate of", input$country),
           x = "Year",
           y = "Exchange Rate")
  })
}

# Step 6: Run the application
shinyApp(ui = ui, server = server)
