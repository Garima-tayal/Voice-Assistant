import PyPDF2
import pyttsx3
pdf_file = open('Sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
speaker = pyttsx3.init()
for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    if text:
        speaker.say(text)
        speaker.runAndWait()
pdf_file.close()
speaker.stop()