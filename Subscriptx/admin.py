class Admin:
    def __init__(self, name):
        self.name = name

    def view_subscriptions(self, subscriptions):
        for sub in subscriptions:
            print(f"{sub.user.name} - {sub.plan.name} - {sub.status}")