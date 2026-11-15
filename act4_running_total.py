
total = 0
count = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    count += 1
    price = float(input("Price (0 to stop): "))

if count > 0:
    average = total / count
    print("Items:", count)
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
else:
    print("No items entered.")
