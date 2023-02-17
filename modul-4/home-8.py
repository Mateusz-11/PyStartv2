products = {
    "doniczka": 15,
    "konewka": 20,
    "grabie": 12,
    "szpadel": 18,
    "kosiarka": 1200,
    "łopata": 22,
    "siekiera": 28,
    "młotek": 12,
    "wiadro": 8,
}
order = {}
choice = "yes"
while choice != "no":
    for product, price in products.items():
        print(product, " - ", price, "zł")
    print("---" * 10)
    if order.keys() != 0:
        print("Your order: ")
        for p, a in order.items():
            print(p, "-", a, "item")
    choice = input("What product do you want add to cart?  ")
    amount = int(input("How many do you want to add this product? "))
    if choice in products.keys():
        order[choice] = amount
    print("---" * 10)
    choice = input("Do you want add new product to the cart? (yes / no): ")

print("---" * 10)
print("Your summary:")
print("*" * 40)
summary = 0
for product, amount in order.items():
    # print(product, "-", amount * products[product], "zł")
    print("| {:16s} | {:16s} |".format(f"{product}", f"{amount * products[product]} zł"))
    summary += amount * products[product]

print("*" * 40)
print(f"Total to pay: {summary} zł")
print("---" * 10)
