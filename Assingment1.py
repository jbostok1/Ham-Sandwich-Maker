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

### Make an instance of SandwichMachine class and write the rest of the codes ###