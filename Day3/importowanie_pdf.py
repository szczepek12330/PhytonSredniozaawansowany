import PyPDF2

output_pdf = PyPDF2.PdfWriter()

file1 = open('raport.pdf', 'rb')
pdf1 = PyPDF2.PdfFileReader(file1)

output_pdf.appendPagesFromReader(pdf1)

file2 = open('report3.pdf', 'rb')
pdf2 = PyPDF2.PdfFileReader(file2)
output_pdf.appendPagesFromReader(pdf2)

with open('rezultat.pdf', 'wb') as out_file:
    output_pdf.write(out_file)

file1.close()
file2.close()