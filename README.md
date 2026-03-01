# Subscription Billing System

A modular subscription billing system in Python, designed to simulate real-world SaaS workflows.

## Features

- **User Management**:     Add and manage users with different roles.
- **Subscription Plans**:  Subscribe to plans, upgrade, and track status.
- **Invoice Generation**:  Generate invoices automatically for users.
- **Tax & Discounts**:     Apply taxes and discount calculations.
- **Payment Processing**:  Record payments, validate, and track transactions.
- **Unit Testing**:        Includes tests to ensure all functionalities work as expected.
- **File-Based Storage**:  Stores data in JSON files for easy simulation.

## Technologies Used:

- Python 3.x
- Object-Oriented Programming (OOP)
- JSON for data storage
- Modular code structure

## Project Structure:

**Subscriptx/**
├── admin.py
├── billing.py
├── config.py
├── discounts.py
├── invoice.py
├── logger.py
├── logs.txt
├── main.py
├── models.py
├── payments.py
├── reports.py
├── storage.py
├── subscriptx_models.py
└── tests.py


## How to Run / Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/Nadiayousaf/Subscription-billing-system.git
````

2. **Navigate to the project folder:**

```bash
cd Subscription-billing-system
```

3. **Run the main program:**

```bash
python main.py
```

---

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is open-source and available under the MIT License.

---

## Demo / Project Output

```
All tests passed!
Nadia subscribed to Basic plan. Status: ACTIVE
Nadia upgraded to Premium plan. Status: ACTIVE
Generating invoice for Nadia for plan Premium
Invoice generated for Nadia, plan: Premium
Payment of 1000 received from Nadia
Discount applied: 10%




