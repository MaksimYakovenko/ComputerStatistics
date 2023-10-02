import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv("data.csv")
x = data[data['special_proposition'] > 0]
average_cost = x["total"].mean()
print(f"The average cost of the goods from s.p. μ {average_cost}")


n = len(x)
confidence_levels = [0.95, 0.99]
confidence_intervals = []
std_error = x["total"].std() / np.sqrt(n)
for confidence_level in confidence_levels:
    margin_of_error = stats.norm.pdf((1 + confidence_level) / 2) * std_error
    confidence_interval = (average_cost - margin_of_error, average_cost + margin_of_error)
    confidence_intervals.append(confidence_interval)

for i, confidence_level in enumerate(confidence_levels):
    print(f"Confidence intervals {confidence_level * 100}%:{confidence_intervals[i]}")


plt.figure(figsize=(10, 6))
plt.hist(x, bins=20, alpha=0.7)
plt.title("Histogram")
plt.xlabel("Price of product")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
