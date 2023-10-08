import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
without_s_p = (data["total"] - data["special_proposition"]).mean()
print(f"Average price of the product without s.p. μ {without_s_p:.2f} grn.")

n = len(data)
std_error = (data['total'] - data['special_proposition']).std() / np.sqrt(n)
confidence_levels = [0.95, 0.99]
z_values = [stats.norm.ppf(1 - (1 - level) / 2) for level in confidence_levels]
confidence_intervals = []
for z in z_values:
    margin_of_error = z * std_error
    confidence_interval = (without_s_p - margin_of_error, without_s_p + margin_of_error)
    confidence_intervals.append(confidence_interval)

for i, confidence_level in enumerate(confidence_levels):
    print(f"Confidence level {confidence_level * 100}%:{confidence_intervals[i]}")

plt.hist(data["total"] - data["special_proposition"], color="black")
plt.xlabel("The price of the product without s.p.")
plt.ylabel("Frequency")
plt.grid(True)
plt.title("Histogram of the cost of goods without s.p.")

def edf(data): # # Empirical distribution function
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, 1 + n) / n
    return x, y

x, y = edf(data['total'] - data['special_proposition'])
plt.figure()
plt.plot(x, y, color="red")
plt.xlabel("The price of the product without s.p.")
plt.ylabel("Empirical probability")
plt.title("Empirical distribution function")
plt.grid(True)
plt.show()
