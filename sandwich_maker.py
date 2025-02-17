class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients) -> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""
        for name in ingredients.keys():
            if self.machine_resources[name] < ingredients[name]:
                print(f"Sorry there is not enough {name}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients) -> None:
        """Deduct the required ingredients from the resources.
                   Hint: no output"""
        for name in order_ingredients.keys():
            self.machine_resources[name] -= order_ingredients[name]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")