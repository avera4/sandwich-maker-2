class Cashier:
    def __init__(self):
        pass

    def process_coins(self) -> float:
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = input("how many large dollars?: ")
        half_dollars = input("how many half dollars?: ")
        quarters = input("how many quarters?: ")
        nickels = input("how many nickels?: ")
        return float(large_dollars) + (float(half_dollars) * 0.5) + (float(quarters) * 0.25) + (float(nickels) * 0.05)

    def transaction_result(self, coins, cost) -> bool:
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print(f"Here is ${coins - cost} in change.")
            return True
        else:
            print("Sorry, that’s not enough money. Money refunded.")
            return False