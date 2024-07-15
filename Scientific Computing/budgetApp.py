class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            items += f"{item['description'][:23]:23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}{total}"

def create_spend_chart(categories):
    # Calculate total spending per category
    spending = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spending.append(total)
    total_spending = sum(spending)
    
    # Calculate percentage spending per category
    percentages = [int((spend / total_spending) * 100) for spend in spending]

    # Create chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Add bottom line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

# Example usage
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

entertainment = Category('Entertainment')
entertainment.deposit(500, 'deposit')
entertainment.withdraw(45.67, 'movies')
entertainment.withdraw(100, 'concert')

print(food)
print(clothing)
print(entertainment)
print(create_spend_chart([food, clothing, entertainment]))
