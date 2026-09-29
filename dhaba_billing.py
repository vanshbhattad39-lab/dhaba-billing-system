import datetime
import time

menu = {
    1: ("Khadhi Paneer", 220),
    2: ("Dal Tadka", 150),
    3: ("Butter Naan", 40),
    4: ("Jeera Rice", 120),
    5: ("Veg Biryani", 180),
    6: ("paratha", 30),
    7: ("lassi", 30),
    8: ("halwa", 60)
}

gst = 5

print("========================================")
print("       DHABA BILLING SYSTEM")
print("========================================")

while True:

    customer = input("\nEnter customer name: ")

    print("\n----------- MENU -----------")
    print("No.  Item                         Price")

    for number, details in menu.items():
        item_name = details[0]
        item_price = details[1]

        spaces = " " * max(1, 28 - len(item_name))

        print(
            number,
            " ",
            item_name + spaces,
            "Rs.",
            item_price
        )

    print("----------------------------")

    cart = []

    while True:

        choice = input("\nEnter item number (0 to finish): ")

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)

        if choice == 0:
            break

        if choice not in menu:
            print("Item not found.")
            continue

        quantity = input("Enter quantity: ")

        if not quantity.isdigit():
            print("Please enter a valid quantity.")
            continue

        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity should be greater than 0.")
            continue

        name = menu[choice][0]
        price = menu[choice][1]

        total = price * quantity

        cart.append([name, price, quantity, total])

        print(name, "x", quantity, "=", total)

    if len(cart) == 0:

        print("\nNo items were ordered.")

        again = input("Next customer? (y/n): ")

        if again.lower() == "y":
            continue
        else:
            print("Program ended.")
            break

    subtotal = 0

    for item in cart:
        subtotal = subtotal + item[3]

    discount = 0

    if subtotal >= 2000:
        discount = 15
    elif subtotal >= 1000:
        discount = 10
    elif subtotal >= 500:
        discount = 5

    discount_amount = subtotal * discount / 100

    amount_after_discount = subtotal - discount_amount

    gst_amount = amount_after_discount * gst / 100

    final_amount = amount_after_discount + gst_amount

    current_time = datetime.datetime.now()
    date_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

    receipt = ""

    receipt += "\n===============================================\n"
    receipt += "              Vansh Dhaba\n"
    receipt += "===============================================\n"

    receipt += "Customer : " + customer + "\n"
    receipt += "Date     : " + date_time + "\n"

    receipt += "-----------------------------------------------\n"
    receipt += "Item                     Price  Qty    Total\n"
    receipt += "-----------------------------------------------\n"

    for item in cart:

        name = item[0]
        price = item[1]
        quantity = item[2]
        total = item[3]

        receipt += name
        receipt += " " * max(1, 25 - len(name))

        receipt += str(price)
        receipt += " " * max(1, 8 - len(str(price)))

        receipt += str(quantity)
        receipt += " " * max(1, 7 - len(str(quantity)))

        receipt += "Rs." + str(total)
        receipt += "\n"

    receipt += "-----------------------------------------------\n"

    receipt += (
        "Subtotal              : Rs."
        + str(round(subtotal, 2))
        + "\n"
    )

    receipt += (
        "Discount ("
        + str(discount)
        + "%)           : Rs."
        + str(round(discount_amount, 2))
        + "\n"
    )

    receipt += (
        "GST ("
        + str(gst)
        + "%)                : Rs."
        + str(round(gst_amount, 2))
        + "\n"
    )

    receipt += "===============================================\n"

    receipt += (
        "FINAL AMOUNT          : Rs."
        + str(round(final_amount, 2))
        + "\n"
    )

    receipt += "===============================================\n"
    receipt += "          Thank you! Visit again :)\n"
    receipt += "===============================================\n"

    print(receipt)

    save = input("Do you want to save the receipt? (y/n): ")

    if save.lower() == "y":

        file_name = (
            "receipt_"
            + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".txt"
        )

        file = open(file_name, "w")


















        file.write(receipt)
        file.close()

        print("Receipt saved as:", file_name)

    next_customer = input(
        "\nDo you want to enter another customer? (y/n): "
    )

    if next_customer.lower() != "y":
        print("\nThank you for using the billing system.")
        break
