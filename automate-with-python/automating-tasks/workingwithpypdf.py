# pypdf helps creating and modifying pdf files
import pypdf
reader = pypdf.PdfReader('Python-Chapter1.pdf')
pages_lenght = len(reader.pages)
print(pages_lenght)