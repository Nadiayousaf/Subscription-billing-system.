class Report:
    def generate(self, subscription):
        print(f"Report: {subscription.user.name} - Plan {subscription.plan.name} - Status {subscription.status}")