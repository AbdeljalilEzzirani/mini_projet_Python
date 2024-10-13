import numpy as np

temperatures = np.array([22.5, 21.0, 23.5, 24.0, 20.0, 19.5, 25.0, 22.0, 24.5, 23.0])
def anallyse_temperature(temperatures):
    mean_temperature = np.mean(temperatures)
    median_temperature = np.median(temperatures)
    std_deviation = np.std(temperatures)
    return mean_temperature, median_temperature, std_deviation



print (anallyse_temperature(temperatures))
# print (mean_temperature)
# print (median_temperature)
# print (std_deviation)
