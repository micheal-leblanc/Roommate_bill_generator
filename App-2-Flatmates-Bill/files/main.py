from PdfReport import PdfReport
from Bill import Bill
from Roommate import Roommate


amount = float(input("What is the total amount of the bill? "))
period = input("What is the billing period? I.E. April 2023: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house? "))

name2 = input("What is the name of the first roommate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house? "))


the_bill = Bill(amount, period)
roommate1 = Roommate(name1, days_in_house1)
roommate2 = Roommate(name2, days_in_house2)

print(f"{roommate1.name} pays ${roommate1.pays(the_bill, roommate2)}")
print(f"{roommate2.name} pays ${roommate2.pays(the_bill, roommate1)}")


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(roommate1, roommate2, the_bill)
