from fpdf import FPDF

# Create a new PDF document
pdf = FPDF(orientation='Portrait', unit='pt', format='A4')

# Add a page
pdf.add_page()

# Add some text
pdf.set_font(family='Times', size=24, style='B')

# Create a cell
pdf.cell(w=0, h=80, txt="Roommates Bill", border=1, align='C', ln=1)
pdf.cell(w=100, h=40, txt="Period:", border=1)
pdf.cell(w=150, h=40, txt="March 2021", border=1)


# Generate PDF
pdf.output("bill.pdf")