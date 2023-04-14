from fpdf import FPDF
import webbrowser


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

        # Create a new PDF document
        pdf = FPDF(orientation='Portrait', unit='pt', format='A4')

        # Add a page
        pdf.add_page()

        # Add icon
        pdf.image(name="files\house.png", w=30, h=30,)

        # Insert a title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Roommates Bill", border=1, align='C', ln=1)

        # Insert period of the bill and value
        pdf.set_font(family='Times', size=20, style='B')
        pdf.cell(w=150, h=40, txt="Billing Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, align='L',)
        pdf.cell(w=0, h=40, txt=f"Total Amount Due: ${bill.amount}", border=0, align='C', ln=1)
       
        # Insert name and amount due for roommate1
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt=roommate1.name, border=0, align='C')
        pdf.cell(w=150, h=25, txt=(f"${roommate1.pays(bill = bill, roommate2=roommate2)}"), border=0, align='C', ln=1)
        
        # Insert name and amount due for roommate2
        pdf.cell(w=100, h=25, txt=roommate2.name, border=0, align='C')
        pdf.cell(w=150, h=25, txt=(f"${roommate2.pays(bill = bill, roommate2=roommate1)}"), border=0, align='C', ln=1)

        # Generate PDF
        pdf.output(f"{bill.period}.pdf")

        # Automatically open the file
        webbrowser.open(url=f"{bill.period}.pdf", new=2, autoraise=True)


the_bill = Bill(amount = 120, period = "April 2023")
john = Roommate(name = "John", days_in_house = 20)
mary = Roommate(name = "Mary", days_in_house = 25)
pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(roommate1=john, roommate2=mary, bill=the_bill)