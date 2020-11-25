import math


def supply():
    print("Write how many cups of coffee you will need:")
    cup_count = int(input())
    print(f"For {cup_count} of coffee you will need:")
    print(f"{cup_count * 200} ml of water")
    print(f"{cup_count * 50} ml of milk")
    print(f"{cup_count * 15} g of coffee beans")


def count_cups():
    coffee_cup = [200, 50, 15]
    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    cups = int(input("Write how many cups of coffee you will need:\n"))
    max_cups = math.floor(
        min(water / coffee_cup[0], milk / coffee_cup[1], beans / coffee_cup[2]))
    if (max_cups - cups == 0):
        print("Yes, I can make that amount of coffee")
    elif (max_cups - cups > 0):
        print(f"Yes, I can make that amount of coffee (and even {max_cups - cups} more than that)")
    else:
        print(f"No, I can make only {max_cups} cups of coffee")


def main():
    count_cups()


if __name__ == "__main__":
    main()