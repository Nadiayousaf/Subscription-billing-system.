class InvoiceGenerator:
    def create_invoice(self, subscription):
        print(f"Generating invoice for {subscription.user.name} for plan {subscription.plan.name}")