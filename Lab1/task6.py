import pandas as pd

data = pd.read_csv("data.csv")

returned_special_proposition = data[(data['special_proposition'] > 0) & (data['return'] == True)]
result = len(returned_special_proposition) * 20
print(f"Total costs of delivery for cases when goods from s.p. returned {result} grn.")

total_profit = (returned_special_proposition["total"] + returned_special_proposition["special_proposition"]) * 1.2
total_profit = total_profit.sum()
print(f"The total profit of these orders {total_profit}")

total_with_free_paid = (returned_special_proposition["total"] + returned_special_proposition["special_proposition"])- 20
total_with_paid_free = (returned_special_proposition["total"] + returned_special_proposition["special_proposition"]) * 1.2
result1 = total_with_paid_free / total_with_free_paid
print(result1)
