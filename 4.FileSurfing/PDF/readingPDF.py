import PyPDF2
file = open('const.pdf', 'rb')
fileReader = PyPDF2.PdfFileReader(file)
# print(fileReader.getObject)
page_1=fileReader.getPage(0)

p_text= page_1.extractText()
# extract data line by line
P_lines=p_text.splitlines()
print P_lines
