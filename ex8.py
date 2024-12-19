people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))
slicesper = pizzas * 8 // people
leftovers = (pizzas * 8) % people

print()
print(f"{people} with {pizzas} pizzas")
print(f"Each person gets {slicesper} pieces of pizza")
print(f"There are {leftovers} leftover pieces")