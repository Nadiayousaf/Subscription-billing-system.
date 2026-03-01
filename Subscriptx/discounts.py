class DiscountManager:
    def get_discount(self, user, plan):
        # Example: 10% discount for Premium
        if plan.name == "Premium":
            return 10
        return 0