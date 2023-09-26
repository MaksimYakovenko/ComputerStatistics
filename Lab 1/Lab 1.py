import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")

print("--------------- Section 1 ---------------")

n = len(data[data['special_proposition'] > 0])
x = len(data[(data['special_proposition'] > 0) & (data['return'] == True)])

probability = x / n
print(f"Probability of returning goods from a special offer: {probability:.2%}")


confidence_levels = [0.95, 0.99] # Levels of trust


confidence_intervals = []
for confidence_level in confidence_levels:
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha / 2)
    margin_of_error = z_critical * np.sqrt(probability * (1 - probability))
    confidence_interval = (probability - margin_of_error, probability + margin_of_error)
    confidence_intervals.append(confidence_interval)

for i, confidence_level in enumerate(confidence_levels):
    print(f"Confidence intervals {confidence_level * 100}%: {confidence_intervals[i]}")


print("--------------- Section 2 ---------------")

special_proposition_data = data[data['special_proposition'] > 0]
average_cost = special_proposition_data['total'].sum() / len(special_proposition_data)
print(f"Average price with a special offer (μ): {average_cost}")
