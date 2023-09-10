from PyPDF2 import PdfReader 

reader = PdfReader("frankenstein.pdf") 
all_pages = reader.pages
# print(all_pages)
all_text = []
for page in all_pages:
    all_text.append(page.extract_text())

full_text_combined = " ".join(all_text) # to combine a set of strings
# print(type(full_text_combined))

individual_words = full_text_combined.split(".") # to split a string
# print(len(individual_words))

for sentence in individual_words:
    if("monster" in sentence):
        print(sentence)



# resize pictures using python / hint: pillow
# read in a word document and do some analysis on the text
# read a .txt file and do some analysis
# Try to create some audio files using python. 