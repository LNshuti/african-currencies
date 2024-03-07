import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall
import os 

# Get number of port calls and trade volume estimates derrived from AIS data for Ukraine in 2020-2023 with vessel types DRY BULK.
df_aistrade = comtradeapicall.getAIS(subscription_key=os.getenv("SUBSCRIPTION_KEY"), countryareaCode=comtradeapicall.convertCountryIso3ToCode('AUS'), vesselTypeCode='1', dateFrom='2020-01-01', dateTo='2023-12-31')

print(df_aistrade)
# plot the mtc (trade volume in metric tons) histogram - in log scale
df_aistrade.hist("mtc", log=True);
plt.xlabel('(log) metric tons')
plt.ylabel('Total seaborne trade')
plt.title('Trade Volume Distribution')
plt.show()

# Get number of port calls and trade volume estimates derrived from AIS data for Ukraine in 2020-2023 with vessel types DRY BULK.
df_aistrade = comtradeapicall.getAIS(subscription_key="895345bf3d5c42c097eb1c98f179d76e", countryareaCode=comtradeapicall.convertCountryIso3ToCode('AUS'), vesselTypeCode='1', dateFrom='2020-01-01', dateTo='2023-12-31')
print(df_aistrade)

# plot the mtc (trade volume in metric tons) histogram - in log scale
df_aistrade.hist("mtc", log=True);
plt.xlabel('(log) metric tons')
plt.ylabel('Total seaborne trade')
plt.title('Trade Volume Distribution')
plt.show()
