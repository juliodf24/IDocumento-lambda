import base64

def word_to_base64(file_path):
    print('gerando base64 do template....')
    with open(file_path, 'rb') as file:
        file_content = file.read()
        TemplateBase64 = base64.b64encode(file_content).decode('utf-8')
        print('base64 do template gerado com sucesso')
        # print(TemplateBase64)
        return TemplateBase64