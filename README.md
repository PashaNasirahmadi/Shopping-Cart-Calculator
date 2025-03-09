README.md
markdown
Copy
# Shopping Cart Calculator

This Python script helps manage a shopping cart by calculating the total price of items, applying discounts for bulk purchases, and adding taxes. Users can input multiple items, their quantities, and prices to get a detailed summary of their purchase.

## Features

- Add multiple items, quantities, and prices.
- Automatically applies a 25% discount for purchases with more than 5 items.
- Adds a fixed tax of 3.5 to each item.
- Displays the total price and a summary of the shopping cart.

## Requirements

- Python 3.x
- `numpy` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Shopping-Cart-Calculator.git
Navigate to the project directory:

bash
Copy
cd Shopping-Cart-Calculator
Install the required dependencies:

bash
Copy
pip install numpy
Usage
Run the script using Python:

bash
Copy
python shopping_cart.py
Follow the on-screen prompts to input items, quantities, and prices. The script will calculate the total cost, apply discounts if applicable, and display a summary.

Example
bash
Copy
$ python shopping_cart.py
تعداد خرید را وارد کنید: 2
خرید مورد نظر را وارد کنید: Apple
تعداد خرید را وارد کنید: 3
قیمت خرید را وارد کنید: 1.5
خرید مورد نظر را وارد کنید: Banana
تعداد خرید را وارد کنید: 2
قیمت خرید را وارد کنید: 2.0
لیست خرید ها: ['Apple', 'Banana']
لیست قیمت ها: [1.5, 2.0]
لیست تعداد خرید ها: [3, 2]
تخفیف وجود ندارد
قیمت کل بدون تخفیف [5.0, 5.5]
your list of buys: ['Apple', 'Banana'] and number of all of goods you buy is: 2 and the total price of all of goods you buy is: 10.5 thanks for come to our shop
and the full salary for the shop is: 10.5
