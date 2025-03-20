from functions.FillTemplate.fillTemplate import fillTemplate
from functions.ExcelToJson.excelToJosn import excel_para_json
from functions.TemplateToBase64.templateToBase64 import word_to_base64
from functions.DocxToPdf.docxToPdf import docxToPdf


print('iniciando processo:')
print('etapa: 1 de 4')

arquivo = "planilha.xlsx"
json_data = excel_para_json('planilha.xlsx') # caminho do arquivo excel


print('etapa: 2 de 4')
TemplateBase64 = word_to_base64("Template.docx") #caminho do template word


print('etapa: 3 de 4')
documents = fillTemplate(json_data, TemplateBase64, "C:\julio\Programacao\IDocumento-lambda\Documentos-Gerados") #caminho do arquivo gerado
print(documents)


print('etapa: 4 de 4')
docxToPdf(documents)
print('concluido')
