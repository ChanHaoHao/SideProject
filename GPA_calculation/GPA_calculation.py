import PyPDF2

pdfFile = open('GPA_English.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pages = []

# this extracts the text from the pdf file
for x in range(pdfReader.numPages):
    pages.append(pdfReader.getPage(x))

# America GPA 4, 3, 2, 1, 0 => 100~80, 70~79, 60~69, 50~59, 0~49
# NTU GPA 100~90 A+, 89~85 A, 84~80 A-, 79~77 B+, 76~73 B, 72~70 B-
#       , 69~67 C+, 66~63 C, 62~60 C-, 0~59

GPA = 0
credits = 0
for x in range(pdfReader.numPages):
    spaces = 0
    text = pages[x].extractText()
    for y in range(len(text)):
        if text[y] == " ":
            spaces+=1
        else:
            spaces=0
        if spaces==3:
            if text[y+1]=="A":
                GPA += 4*int(text[y-3])
                credits += int(text[y-3])
            elif text[y+1]=="B":
                GPA += 3*int(text[y-3])
                credits += int(text[y-3])
            elif text[y+1]=="C":
                GPA += 2*int(text[y-3])
                credits += int(text[y-3])

print(GPA/credits)