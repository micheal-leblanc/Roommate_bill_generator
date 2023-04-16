from fpdf import FPDF
import webbrowser


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
        pdf.image(name="App-2-Flatmates-Bill/files/house.png", w=30, h=30,)

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