import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        response = input("What would you like? (small/ medium/ large/ off/ report): ")

        match response:
            case "small" | "medium" | "large":
                if not sandwich_maker_instance.check_resources(recipes[response]["ingredients"]):
                    continue
                if cashier_instance.transaction_result(cashier_instance.process_coins(), recipes[response]["cost"]):
                    sandwich_maker_instance.make_sandwich(response, recipes[response]["ingredients"])
            case "off":
                break
            case "report":
                r = ""
                for name, num in sandwich_maker_instance.machine_resources.items():
                    r += f"{name}: {num} {"pound(s)" if name == "cheese" else "slice(s)"}\n"
                print(r, end="")
            case _:
                print("Invalid input! Try again.")

if __name__=="__main__":
    main()
