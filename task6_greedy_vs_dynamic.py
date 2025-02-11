items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Sort by descending calories per unit cost
def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]['calories'] / x[1]['cost'],
        reverse=True
    )
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            chosen_items.append(item)
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item, info = item_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    total_calories = dp[n][budget]
    w = budget
    chosen_items = []
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item, _ = item_list[i - 1]
            chosen_items.append(item)
            w -= items[item]['cost']
    
    return chosen_items, total_calories

budget = 100
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)


print("Budget:", budget)
print("Greedy:")
print("Chosen products:", greedy_result[0])
print("Kcal:", greedy_result[1])

print("\nDynamic:")
print("Chosen products:", dp_result[0])
print("Kcal:", dp_result[1])
print("---Interesting that here you can observe different kcal value.\n")


budget = 279
greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)
print("Budget:", budget)
print("Greedy:")
print("Chosen products:", greedy_result[0])
print("Kcal:", greedy_result[1])

print("\nDynamic:")
print("Chosen products:", dp_result[0])
print("Kcal:", dp_result[1])