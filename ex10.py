pi1 = int(input("Enter the price of item 1: "))
qi1 = int(input("Enter the quantity of item 1: "))
pi2 = int(input("Enter the price of item 2: "))
qi2 = int(input("Enter the quantity of item 2: "))
pi3 = int(input("Enter the price of item 3: "))
qi3 = int(input("Enter the quantity of item 3: "))
subtotal = pi1 * qi1 + pi2 * qi2 + pi3 * qi3
printsubtotal = f"{subtotal:.2f}"
tax = subtotal * 0.055
printtax = f"{tax:.2f}"
total = subtotal + tax
printtotal = f"{total:.2f}"
print(f"Subtotal: ${printsubtotal}")
print(f"Tax: ${printtax}")
print(f"Total: ${printtotal}")