import base64
import io
import os
from docxtpl import DocxTemplate

def fillTemplate(json_alunos, template_base64, output_folder):
    template_bytes = base64.b64decode(template_base64)

    final_path = os.path.join(output_folder, 'Arquivos_Criados')

    os.makedirs(final_path, exist_ok=True)

    zip_io = io.BytesIO()

    #generate docx for each student
    document_list = []
    document_list.append(final_path)
    cont = 0
    for aluno in json_alunos:
        cont  += 1
        # Load DOCX template from memory
        doc_io= io.BytesIO(template_bytes)
        doc = DocxTemplate(doc_io)
        doc.render(aluno)

        file_name = f"{aluno['Matricula']}_Documneto"
            
        doc.save(os.path.join(final_path, file_name + '.docx'))
        document_list.append(file_name)
    print("arquivos criados: ", cont)

    return document_list