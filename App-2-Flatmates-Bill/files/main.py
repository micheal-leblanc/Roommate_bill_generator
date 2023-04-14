class Bill:
    """
    Object that contains data about the bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    """
    Creates a roommate who lives in the house and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount / 2

class PdfReport:
    """
    Creates a PDF file that contains data about the roommates such as their names, their amount due and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, roommate1, roommate2, bill):
        pass


the_bill = Bill(amount = 120, period = "March 2021")
john = Roommate(name = "John", days_in_house = 20)
mary = Roommate(name = "Mary", days_in_house = 25)

print(john.pays(bill = the_bill))