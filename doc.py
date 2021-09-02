from docxtpl import DocxTemplate

from docxtpl import DocxTemplate
doc = DocxTemplate("report.docx")
context = {'marka_avto': 'BMW', 'model_avto': '7', 'rashod': '17 л', 'price': '15 700 000'}
doc.render(context)
doc.save("шаблон-final.docx")