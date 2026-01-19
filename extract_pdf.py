import pypdf

pdf_path = r'c:\Users\Tanvi Patel\Desktop\Code\Tanu1007.github.io\Tanvi_Patel_resume.pdf'
pdf = pypdf.PdfReader(pdf_path)
text = '\n'.join([page.extract_text() for page in pdf.pages])
print(text)
