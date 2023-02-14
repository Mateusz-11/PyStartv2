
list_of_email = []
for _ in range(3):
    new_email = input("Write new email: ")
    if "@" in new_email:
        list_of_email.append(new_email)

set_of_emails = set(list_of_email)
print(set_of_emails)
print(f"You add {len(list_of_email)} emails.")
print((f"You add {len(set_of_emails)} emails (without duplicate)"))