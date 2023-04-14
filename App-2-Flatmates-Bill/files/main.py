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

    def pays(self, bill, roommate2):
        """Creates a coefficient based on amount of days stayed in the house and multiplies bill amount by weight"""
        weight = self.days_in_house / (self.days_in_house + roommate2.days_in_house)

        amount_to_pay = bill.amount * weight
        # Rounds float to two decimal places and returns as string
        return "{:.2f}".format(amount_to_pay) 
    
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

print(f"John pays ${john.pays(bill=the_bill, roommate2=mary)}")
print(f"Mary pays ${mary.pays(bill=the_bill, roommate2=john)}")
print(f"Total bill is ${the_bill.amount} for {the_bill.period}")