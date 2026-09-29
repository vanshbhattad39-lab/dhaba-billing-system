Vansh Dhaba Billing System

A simple Python-based dhaba billing system designed to make dhaba bill calculation easier.

Description

This project allows a dhaba to enter customer details, display a food menu, take orders, calculate the total price, apply discounts, calculate GST, and generate a final bill.

The program can also save the generated receipt as a text file for future reference.

Features

- Displays a dhaba menu
- Takes customer name
- Allows the customer to select multiple items
- Takes quantity for each item
- Calculates the price of each ordered item
- Calculates the subtotal
- Applies discount based on the bill amount
- Calculates GST
- Generates a formatted receipt
- Saves the receipt in a ".txt" file
- Supports multiple customers
- Handles invalid item numbers and quantities

Discount System

The program provides discounts according to the subtotal:

Subtotal| Discount
₹500 or more| 5%
₹1000 or more| 10%
₹2000 or more| 15%

GST

A GST rate of 5% is applied after the discount has been deducted.

Menu

No.| Item| Price
1| Khadi Paneer| ₹220
2| Dal Tadka| ₹150
3| Butter Naan| ₹40
4| Jeera Rice| ₹120
5| Veg Biryani| ₹180
6| paratha| ₹30
7| Lassi| ₹30
8| Halwa| ₹60

Technologies Used

- Python
- Dictionaries
- Lists
- Loops
- Conditional statements
- User input
- String formatting
- File handling
- Date and time

How to Run

Make sure Python is installed on your computer.

Open a terminal in the project folder and run:

python restaurant_billing.py

The program will then ask for the customer's name and display the dhaba menu.

Receipt

After completing an order, the program generates a receipt containing:

- Customer name
- Date and time
- Ordered items
- Item prices
- Quantities
- Individual totals
- Subtotal
- Discount
- GST
- Final amount

The user can choose whether to save the receipt as a text file.

Project Structure

vansh-restaurant-billing-system/
│
├── restaurant_billing.py
└── README.md

Author

Vansh

Project Type

Academic / Python Programming Project
