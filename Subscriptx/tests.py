from subscriptx_models import User, Plan, Subscription
def test_subscription_expiry():
    user = User(1, "Test", "test@test.com")
    plan = Plan(1, "Basic", 1000, 0)
    sub = Subscription(user, plan)
    assert sub.check_status() == "EXPIRED"

print("All tests passed!")