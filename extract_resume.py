from pdfminer.high_level import extract_text
p = 'Shantanu_DA_Resume.pdf'
text = extract_text(p)
open('resume_extracted.txt','w',encoding='utf-8').write(text)
print(text[:6000])
