import random
import matplotlib.pyplot as plt

def roll_two_dices():
    return random.randint(1, 6) + random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    result_counts = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_rolls):
        total = roll_two_dices()
        result_counts[total] += 1
    
    probabilities = {k: v / num_rolls * 100 for k, v in result_counts.items()}
    return probabilities

num_rolls = 100000
monte_carlo_probabilities = monte_carlo_simulation(num_rolls)

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

sums = list(monte_carlo_probabilities.keys())
monte_carlo_values = list(monte_carlo_probabilities.values())
analytical_values = [analytical_probabilities[sum] for sum in sums]

plt.plot(sums, monte_carlo_values, label="monte_carlo", marker='o')
plt.plot(sums, analytical_values, label="analytical", marker='x')

plt.xlabel("two dices sum")
plt.ylabel("probability (%)")
plt.title("probability of two dices sum")
plt.legend()
plt.grid(True)
plt.show()
