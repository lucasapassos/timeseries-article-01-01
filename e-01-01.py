# Use the attribute Trend of the seasonal_decompose object to
# access the trend values obtained. Use the plot() method to plot it
trend = decompose.trend
trend.plot()

# Use the attribute Seasonal of the seasonal_decompose object to
# access the seasonal values obtained. Use the plot() method to plot it
season = decompose.seasonal
season.plot()

# Use the attribute resid of the seasonal_decompose object to
# access the residuals values obtained. Use the plot() method to plot it
resid = decompose.resid
resid.plot();

