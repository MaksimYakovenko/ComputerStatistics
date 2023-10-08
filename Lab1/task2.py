import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv("data.csv")
prices = data["special_proposition"]
average_cost = prices.mean()
print(f"The average cost of the goods from s.p. μ {average_cost}")


n = len(prices)
std_error = prices.std() / np.sqrt(n)
confidence_levels = [0.95, 0.99]
confidence_intervals = []
for confidence_level in confidence_levels:
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z_critical * std_error
    confidence_interval = (average_cost - margin_of_error, average_cost + margin_of_error)
    confidence_intervals.append(confidence_interval)

for i, confidence_level in enumerate(confidence_levels):
    print(f"Confidence level {confidence_level * 100}% для μ:{confidence_intervals[i]}")


plt.hist(prices, color="black")
plt.title("Histogram")
plt.xlabel("The price of the product according to s.p.")
plt.ylabel("Frequency")
plt.title("The histogram of the prices of goods by s.p.")
plt.grid(True)


def edf(data): # Empirical distribution function
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y

x, y = edf(prices)
plt.figure()
plt.plot(x, y, color="r")
plt.title("Empirical distribution function")
plt.xlabel("The price of the product according to s.p.")
plt.ylabel("Empirical probability")
plt.grid(True)
plt.show()
