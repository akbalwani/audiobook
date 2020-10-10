import pyttsx3
import PyPDF2

book = open('object.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

pagecount = pdfReader.numPages
print(pagecount)
speaker = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
print(text)
speaker.say(text)
speaker.runAndWait()