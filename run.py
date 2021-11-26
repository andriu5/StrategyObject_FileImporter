from ImportEngine import Importer

print("1. .pdf: ",Importer.parse('./data/cats.pdf'))
# print("2. .csv: ",Importer.parse('./data/cats.csv'))
gatos = Importer.parse('./data/cats.csv')
print("2. .csv: ",gatos, type(gatos))
print("2.1 nombre gato: ",gatos[0].name," edad: ",gatos[0].age, "is ",gatos[0].isIndoor)
print("2.2 nombre gato: ",gatos[1].name," edad: ",gatos[1].age, "is ",gatos[1].isIndoor)
print("2.3 nombre gato: ",gatos[2].name," edad: ",gatos[2].age, "is ",gatos[2].isIndoor)
print("3. .docx: ",Importer.parse('./data/cats.docx'))
print("4. .xls: ",Importer.parse('./data/cats.xls'))
print("5. .xlsx: ",Importer.parse('./data/cats.xlsx'))
print("6. .txt: ",Importer.parse('./data/cats.txt'))