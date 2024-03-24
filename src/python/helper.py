
import requests
import csv
import os
from datetime import datetime

class ExchangeRateDownloader:
    def __init__(self, api_credentials):
        self.api_url = 'https://xecdapi.xe.com/v1/'
        self.api_credentials = api_credentials
        self.african_countries = self._get_african_countries()

    def _get_african_countries(self):
        # Assuming there's a method in XCDRatesClient to get a list of countries
        # This is a placeholder list, the actual implementation should fetch from the API
        return ['DZD', 'EGP', 'NGN', 'ZAR', 'KES'] # Add all African country codes here

    def _fetch_exchange_rates(self, base_currency, target_currency, start_date, end_date):
        # Implement the logic to fetch exchange rates using XCDRatesClient
        # This is a placeholder implementation
        response = requests.get(f'{self.api_url}historical_rate/{base_currency}/{target_currency}',
                                auth=self.api_credentials,
                                params={'start_date': start_date, 'end_date': end_date})
        return response.json()

    def download_rates(self, start_date, end_date):
        rates_data = []
        for country in self.african_countries:
            rates = self._fetch_exchange_rates(country, 'USD', start_date, end_date)
            rates_data.append(rates)

        self._save_to_csv(rates_data)

    def _save_to_csv(self, rates_data):
        file_path = '/mnt/data/exchange_rates.csv'
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # Assuming each rate data contains date and rate
            writer.writerow(['Date', 'Base Currency', 'Target Currency', 'Rate'])
            for data in rates_data:
                for rate in data['rates']:
                    writer.writerow([rate['date'], data['base_currency'], 'USD', rate['rate']])
        print(f"Exchange rates saved to {file_path}")

# Example usage (replace with actual API credentials)
api_credentials = ('username', 'password')
downloader = ExchangeRateDownloader(api_credentials)
downloader.download_rates('2023-01-01', '2024-01-01')
