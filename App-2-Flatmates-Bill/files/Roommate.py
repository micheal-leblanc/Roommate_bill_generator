class Roommate:
    """
    Creates a roommate who lives in the house and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, roommate2):
        """Creates a coefficient based on amount of days stayed in the house and multiplies bill amount by weight"""
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)

        amount_to_pay = bill.amount * weight
        # Rounds float to two decimal places and returns as string
        return "{:.2f}".format(amount_to_pay)