import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall
import os 

comtrade_api = os.getenv("SUBSCRIPTION_KEY")
# Get number of port calls and trade volume estimates derrived from AIS data for Ukraine in 2020-2023 with vessel types DRY BULK.
df_aistrade = comtradeapicall.getAIS(
        subscription_key=comtrade_api,
        countryareaCode=comtradeapicall.convertCountryIso3ToCode('ZAF'), 
        vesselTypeCode='1',
        dateFrom='2020-01-01',
        dateTo='2023-12-31'
        )

# print(df_aistrade)
# # plot the mtc (trade volume in metric tons) histogram - in log scale
# df_aistrade.hist("mtc", log=True);
# plt.xlabel('(log) metric tons')
# plt.ylabel('Total seaborne trade')
# plt.title('Trade Volume Distribution')
# plt.show()


# plot the mtc (trade volume in metric tons) histogram - in log scale
# df_aistrade.hist("mtc", log=True);
# plt.xlabel('(log) metric tons')
# plt.ylabel('Total seaborne trade')
# plt.title('Trade Volume Distribution')
# plt.show()

#change to date format, and add year_month column
df_aistrade["date"] = pd.to_datetime(df_aistrade["date"]) # Convert Date column to datetime format
df_aistrade["year_month"] = df_aistrade["date"].dt.to_period("M")
df_aistrade["month"] = df_aistrade["date"].dt.strftime('%m') + '(' + df_aistrade["date"].dt.strftime('%b') +')'
df_aistrade["year"] = df_aistrade["date"].dt.year

#preparing for plotting
df_aistrade_group = df_aistrade.groupby(['year', 'month']).agg({'mtc': ['sum', 'min', 'max']})
df_aistrade_group.columns = ['mtc_sum', 'mtc_min', 'mtc_max']
df_aistrade_group = df_aistrade_group.reset_index()
df_aistrade_pivot = df_aistrade_group.pivot(index='month', columns='year')['mtc_sum']

#plot the data to show year-to-year trade volume in Ukraine
df_aistrade_pivot.plot()
plt.title('Trade Volume Estimates - Bulk Dry (2020-2023)')
plt.ylabel('metric tons (mtc)')
plt.xlabel('Month')
plt.show()
