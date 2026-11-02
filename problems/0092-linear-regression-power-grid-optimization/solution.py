import math
from sklearn.linear_model import LinearRegression

PI = 3.14159
import numpy as np
def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	consumption_data=np.asarray(consumption_data)
	consumption_data=consumption_data-(10*np.sin(2*PI*(np.arange(1, 11, 1))/10))
	lr=LinearRegression()
	lr.fit((np.arange(1, 11, 1)).reshape(-1,1),consumption_data)
	ypred=lr.predict(np.array([[15]])).item()
	ypred=round(ypred+(10*np.sin(2*PI*15/10)))
	ypred=1.05*ypred
	return math.ceil(ypred)