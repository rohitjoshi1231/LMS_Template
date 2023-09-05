from plans.plan import Plan


class Payment(Plan):
    def __init__(self, plan_name: str, price: int):
        self.plan_name = plan_name
        super().__init__(price)
    # Add and store payment details in database
