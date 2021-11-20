from ImportEngine import Importer

print("1. .pdf: ",Importer.parse('./data/cats.pdf'))
print("2. .csv: ",Importer.parse('./data/cats.csv'))
print("3. .docx: ",Importer.parse('./data/cats.docx'))
print("4. .xls: ",Importer.parse('./data/cats.xls'))
print("5. .xlsx: ",Importer.parse('./data/cats.xlsx'))
print("6. .txt: ",Importer.parse('./data/cats.txt'))