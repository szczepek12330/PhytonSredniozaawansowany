from fpdf import FPDF

document = FPDF()

document.set_font('Times', "B", 14)
document.set_text_color(19, 83, 173)
document.add_page()
document.cell(0, 5, 'Testowy dokument PDF')
document.ln()

document.set_font('Times', '', 12)
document.set_text_color(0)
document.multi_cell(0, 5, 'To jest przykladowy dlugi akapit' * 10)
document.ln()

document.output('raport.pdf')