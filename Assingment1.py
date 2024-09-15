### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}



### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        """this is a for loop that checkls if there is a resource, if not, it returns a statement saying what is missing."""
        for item in ingredients:
            if ingredients[item] > self.machine_resource[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        """This is a basic process function that prompts the user to input coins, and then returns the total of what was input."""

        print("Please insert coins: ")
        large_dollars = int(input("How many large dollars?: ")) * 1
        half_dollars = int(input("How many large dollars?: ")) * .5
        quarters = int(input("How many large dollars?: ")) * .25
        nickels = int(input("How many large dollars?: ")) * .05
        total = large_dollars + half_dollars + quarters + nickels
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        """This function shows the result of a successful/unsuccessful transaction"""

        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"here is ${change} in change.")
            return True
        else:
            print("Sorry, not enough money. You have been refunded!")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size.capitalize()} sandwich is ready! Enjoy!")

    def sandwich_Report(self):
        """Displays current ingredients"""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounces")

machine_resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24  # ounces
}
sandwich_machine = SandwichMachine(machine_resources)

# Sample interaction loop
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        sandwich_machine.report()
    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid choice. Please select again.")


