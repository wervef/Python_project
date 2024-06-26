from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(input_file, output_directory):
    # Read the content of the .txt file
    with open(input_file, 'r') as txt_file:
        txt_content = txt_file.read()

    # Create a PDF file
    pdf_file = f"{output_directory}/output.pdf"

    # Generate PDF
    c = canvas.Canvas(pdf_file, pagesize=letter)
    text_object = c.beginText(100, 750)
    text_object.setFont("Helvetica", 12)
    lines = txt_content.split('\n')
    for line in lines:
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()

    print(f"PDF file saved at: {pdf_file}")


input_file = r"C:/Users/user\Desktop/file.txt" 
output_directory = r"C:/Users/user\Desktop" 
txt_to_pdf(input_file, output_directory)
