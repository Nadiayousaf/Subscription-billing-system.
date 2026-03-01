from datetime import date, timedelta

# --------------------------
# User Class
# --------------------------
class User:
    def __init__(self, user_id, name, email, role="customer"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role

# --------------------------
# Plan Class
# --------------------------
class Plan:
    def __init__(self, plan_id, name, price, duration_days):
        self.plan_id = plan_id
        self.name = name
        self.price = price
        self.duration_days = duration_days

# --------------------------
# Subscription Class
# --------------------------
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