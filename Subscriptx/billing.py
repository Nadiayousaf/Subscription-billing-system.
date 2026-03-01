from invoice import InvoiceGenerator

class Billing:
    def __init__(self, subscription):
        self.subscription = subscription

    def generate_invoice(self):
        invoice = InvoiceGenerator()
        invoice.create_invoice(self.subscription)
        print(f"Invoice generated for {self.subscription.user.name}, plan: {self.subscription.plan.name}")