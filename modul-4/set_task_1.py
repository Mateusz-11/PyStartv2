
items_set = set()
for _ in range(5):
    new_item = input("What you want to add? ")
    if new_item in items_set:
        print("The item is already in you set")
    else:
        items_set.add(new_item)
        print(f"You have: {items_set}")
