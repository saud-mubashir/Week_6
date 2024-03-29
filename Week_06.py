# Welcome to the Building Materials Store

print("\t\t\t\t    Main Menu")
print("\t\t-------------------------------------------------------------------")
print("\t\t|    CODE\t|    ITEMS \t|     WEIGHT RANGE   |   PRICES     |")
print("\t\t|\t\t|\t\t|\t\t    |\t\t   |")
print("\t\t|     C\t\t|    Cement \t| 24.9KG to 25.1KG  |\t  3$\t   |")
print("\t\t|     S\t\t|    Sand \t| 49.5KG to 50.1KG  |\t  2$\t   |")
print("\t\t|     G\t\t|    Gravel\t| 49.5KG to 50.1KG  |\t  2$\t   |")
print("\t\t-------------------------------------------------------------------\n")

# User Input Section
c_sack = int(input("\t\tEnter the number of cement sacks: "))
g_sack = int(input("\t\tEnter the number of gravel sacks: "))
s_sack = int(input("\t\tEnter the number of sand sacks: "))

# Initial Calculations
actual_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2)
total_order = c_sack + g_sack + s_sack

rejected_sacks = 0
total_weight = 0

# Sack Inspection Loop
for count in range(1, total_order + 1):
    print()
    content = input("\t\tEnter the content of a sack (C for cement, G for gravel, S for sand): ").upper()

    if content == 'C':
        while True:
            weight = float(input("\t\tEnter weight of cement sack between 24.9KG and 25.1KG: "))
            if 24.9 <= weight <= 25.1:
                break
            else:
                print("\t\tSack is underweight or overweight")
    elif content == 'G' or content == 'S':
        while True:
            weight = float(input(f"\t\tEnter weight of {content} sack between 49.0KG and 50.1KG: "))
            if 49.0 <= weight <= 50.1:
                break
            else:
                print(f"{content}\t\tsack is underweight or overweight")
    else:
        print("\t\tThe entered content is incorrect")

    total_weight += weight

# Final Output Section
print()
print("\t\tThe total weight of the order is:", total_weight)
print("\t\tThe number of rejected sacks is:", rejected_sacks)

# Special Pack Section
special_packs = 0
special_pack_price = 0

while c_sack >= 1 and g_sack >= 2 and s_sack >= 2:
    special_packs += 1
    c_sack -= 1
    g_sack -= 2
    s_sack -= 2

if special_packs >= 1:
    special_pack_price = special_packs * 10
    print("\t\tTotal special packs are:", special_packs)
    print("\t\tPrice of special packs in dollars is: $", special_pack_price)

    discounted_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2) + special_pack_price
    print("\t\tThe actual price of the order is: $", actual_price)
    print("\t\tThe discounted price of the order is: $", discounted_price)

    total_discount = actual_price - discounted_price
    print("\t\tTotal discount in the order is: $", total_discount)
else:
    print("\t\tPrice of the regular order in dollars is: $", actual_price)
