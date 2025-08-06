# SauceDemo Checkout Automation Test

This project is an end-to-end UI automation test script using **Selenium WebDriver** in Python. It simulates a user interaction flow on the [SauceDemo](https://www.saucedemo.com/) website — from login to completing a checkout process — and validates the successful transaction.

## 🧪 Features Tested

- Login with standard user credentials
- Add multiple items to cart
- Proceed to checkout
- Fill in user information
- Complete the purchase
- Validate that the "Thank You" page appears after a successful order

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- ChromeDriver

## 🧾 How to Run

1. Make sure Python and ChromeDriver are installed.
2. Install Selenium:
   ```bash
   pip install selenium
   ```
3. Run the script:
   ```bash
   python test.py
   ```

## ✅ Assertion

At the end of the checkout process, the script asserts whether the **"Thank you for your order!"** message appears to confirm a successful transaction.
