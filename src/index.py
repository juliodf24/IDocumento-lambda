import os
from functions.FillTemplates.fillTemplate import fillTemplate
from functions.ExcelToJson.excelToJosn import excel_para_json
from functions.TemplateToBase64.templateToBase64 import word_to_base64



print('iniciando processo:')
print('etapa: 1 de 4')
arquivo = "planilha.xlsx"
# planilha = os.path.abspath(arquivo)
# print(planilha)
json_data = excel_para_json('planilha.xlsx') # caminho do arquivo excel
print('etapa: 2 de 4')
# arquivo = "Template.docx"
# template = os.path.abspath(arquivo)
# print(template)
TemplateBase64 = word_to_base64("Template.docx") #caminho do template word
print('etapa: 3 de 4')
zip_content = fillTemplate(json_data, TemplateBase64)
print('etapa: 4 de 4')
zip_file_name = str('Documentos-Gerados') + ".zip"
with open(zip_file_name, 'wb') as f:
    f.write(zip_content)
print('concluido')