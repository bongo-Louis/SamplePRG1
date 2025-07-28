# Functions Functions Functions
# Name : Louis Hoe Zheng Sheng
# Student ID : S10271008D

# read snack name and price from a file
def read_snacks_file(filename):
    snack_names = []
    snack_prices = []
    with open(filename, 'r') as file:
        for line in file:
            name, price = line.strip().split(',')
            snack_names.append(name)
            snack_prices.append(float(price))
    return snack_names, snack_prices

# get a valid snack budget from the user
def get_valid_budget():
    while True:
        budget = float(input("Enter your snack budget: "))
        if budget <= 0:
            print("Your budget is too low! Try asking the office for a raise.")
        else:
            return budget

# classify the snack based on its price
def classify_snack(price):
    if price < 2.0:
        return "Healthy snack"
    elif 2.0 <= price <= 5.0:
        return "Snack of the Gods"
    else:
        return "Luxury snack"

snack_names, snack_prices = read_snacks_file("snack_price.txt")

budget = get_valid_budget()

# Check for affordable snacks
affordable_snacks = []
for i in range(len(snack_names)):
    if snack_prices[i] <= budget:
        affordable_snacks.append((snack_names[i], snack_prices[i]))

# Check if any snacks are affordable
if not affordable_snacks:
    print("Your budget is too low for any snacks. Try asking the office for a raise.")
else:
    print("Here’s what you can buy:")
    with open("snack_list.txt", 'w') as output_file:
        for name, price in affordable_snacks:
            category = classify_snack(price)
            print(f"- {name} (${price:.2f}) - {category}")
            output_file.write(f"{name},{price:.2f}\n")
    print("Your snack list has been saved to 'snack_list.txt'.")