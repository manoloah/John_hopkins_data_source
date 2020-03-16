from fetch_data import df_confirmed, df_death, df_recovered
import matplotlib.pyplot as plt
import pandas as pd


def data_type(data):
	# get metadata (columns that describe the timeseries data)
	metadata = data.iloc[:,:4]

	# get date information and indexing data by country or region
	timeseries = data.set_index(data["Country/Region"]).drop(metadata.columns,axis=1)

	return metadata, timeseries

# Use case for Confirmed
metadata, timeseries = data_type(df_confirmed)

country = "Mexico"

# data of a particular country
country_data = timeseries.loc[country]
country_data.index = pd.to_datetime(country_data.index)

plt.title("Confirmed cases in {country} as of {today}".format(country=country,today=country_data.index[-1].date()))
plt.xticks(rotation=45)
plt.plot(country_data)
plt.show()

