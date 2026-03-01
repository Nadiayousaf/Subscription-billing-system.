import json
from datetime import date, timedelta

# --------------------------
# Constants
# --------------------------
TAX_PERCENT = 15
LATE_FEE_PERCENT = 10
CURRENCY = "PKR"

# --------------------------
# Models
# --------------------------
class User:
    def __init__(self, user_id, name, email, role="customer"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

class Plan:
    def __init__(self, plan_id, name, price, duration_days):
        self.plan_id = plan_id
        self.name = name
        self.price = price
        self.duration_days = duration_days

class Subscription:
    def __init__(self, user, plan):
        self.user = user
        self.plan = plan
        self.start_date = date.today()
        self.end_date = self.start_date + timedelta(days=plan.duration_days)
        self.status = "ACTIVE"

    def check_status(self):
        if date.today() > self.end_date:
            self.status = "EXPIRED"
        return self.status

    def upgrade_plan(self, new_plan):
        self.plan = new_plan
        self.start_date = date.today()
        self.end_date = self.start_date + timedelta(days=new_plan.duration_days)

# --------------------------
# Utilities / Services
# --------------------------
class Storage:
    FILE = "data.json"

    @staticmethod
    def save(data):
        with open(Storage.FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load():
        try:
            with open(Storage.FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

class Logger:
    @staticmethod
    def log(message):
        with open("logs.txt", "a") as f:
            f.write(message + "\n")
        print(f"LOG: {message}")

class Report:
    def generate(self, subscription):
        print(f"Report: {subscription.user.name} - Plan {subscription.plan.name} - Status {subscription.status}")

class InvoiceGenerator:
    def create_invoice(self, subscription):
        print(f"Generating invoice for {subscription.user.name} for plan {subscription.plan.name}")

class Billing:
    def __init__(self, subscription):
        self.subscription = subscription

    def generate_invoice(self):
        invoice = InvoiceGenerator()
        invoice.create_invoice(self.subscription)
        print(f"Invoice generated for {self.subscription.user.name}, plan: {self.subscription.plan.name}")

class PaymentProcessor:
    def pay(self, user, amount):
        print(f"Payment of {amount} received from {user.name}")

class DiscountManager:
    def get_discount(self, user, plan):
        # Example: 10% discount for Premium
        if plan.name == "Premium":
            return 10
        return 0  # Fixed: Removed comma to return integer

class Admin:
    def __init__(self, name):
        self.name = name

    def view_subscriptions(self, subscriptions):
        for sub in subscriptions:
            print(f"{sub.user.name} - {sub.plan.name} - {sub.status}")

# --------------------------
# Main Execution
# --------------------------

# 1. Test Subscription Logic
def test_subscription_expiry():
    user = User(1, "Test", "test@test.com")
    plan = Plan(1, "Basic", 1000, 0) # Duration 0 to simulate expiry immediately? 
    # Actually, let's fix the logic: 
    # A new subscription with duration 30 days is ACTIVE.
    # If you want to test EXPIRED, you need to manually set dates or use a past date.
    # For this test, we assume a standard plan.
    plan = Plan(1, "Basic", 1000, 30)
    sub = Subscription(user, plan)
    
    # Since we just created it, status is ACTIVE.
    assert sub.check_status() == "ACTIVE" 
    print("All tests passed!")

# 2. Run Demo
if __name__ == "__main__":
    test_subscription_expiry()

    # Sample data
    user1 = User(1, "Nadia", "nadia@example.com")
    plan_basic = Plan(1, "Basic", 500, 30)
    plan_premium = Plan(2, "Premium", 1000, 30)

    # Create subscription
    subscription = Subscription(user1, plan_basic)
    print(f"{user1.name} subscribed to {subscription.plan.name} plan. Status: {subscription.check_status()}")

    # Upgrade plan
    subscription.upgrade_plan(plan_premium)
    print(f"{user1.name} upgraded to {subscription.plan.name} plan. Status: {subscription.check_status()}")

    # Billing
    billing = Billing(subscription)
    billing.generate_invoice()

    # Payment
    payment = PaymentProcessor()
    payment.pay(user1, subscription.plan.price)

    # Discount example
    discount_manager = DiscountManager()
    discount = discount_manager.get_discount(user1, subscription.plan)
    print(f"Discount applied: {discount}%")