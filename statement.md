Problem Solving

Manual billing processes in small Dhabas are often time-consuming, prone to calculation errors, and make it difficult to keep track of receipts. Small food business owners need a simple, fast, and automated way to take customer orders, accurately calculate totals including taxes and discounts, and generate professional receipts without relying on expensive or complex software.

Scope of the project

This project is a Python-based Command Line Interface (CLI) application designed to handle the billing process for a dhaba. The scope includes displaying a fixed menu, taking customer orders, calculating subtotals, applying tiered discounts based on the purchase amount, calculating GST, and generating a formatted text receipt. It also includes the functionality to save these receipts locally as text files. The project currently relies on a hardcoded menu and local file system storage, meaning it does not include a graphical user interface (GUI) or an external database for inventory management.

Target users

Cashiers and Billing Staff: Who need a quick and easy tool to calculate totals and generate bills for customers.

Small Dhaba Owners: Who want a lightweight, cost-effective digital solution to manage daily billing and keep digital records of transactions.

Food Stall Operators: Who need a fast way to process orders during peak hours.

High-level features

Interactive Menu Display: Clearly presents available food items and their prices to the user.

Order Management: Allows users to easily add items to a cart by inputting the item number and desired quantity.

Automated Calculations: Automatically calculates item totals, overall subtotal, and applies a flat 5% GST.

Tiered Discount System: Automatically applies discounts based on the cart total (5% for ₹500+, 10% for ₹1000+, and 15% for ₹2000+).

Detailed Receipt Generation: Creates a nicely formatted receipt including the customer's name, date, time, itemized breakdown, and final cost.

Receipt Archiving: Provides an option to save the generated receipt as a timestamped .txt file on the local system for future reference.

Continuous Operation Loop: Allows the cashier to immediately process the next customer without needing to restart the application.
