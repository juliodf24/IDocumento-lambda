import base64
import io
import zipfile
from docxtpl import DocxTemplate

def fillTemplate(json_alunos, template_base64):
    template_bytes = base64.b64decode(template_base64)
    # create a zip file in memory
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, 'w', zipfile.ZIP_DEFLATED) as zipf:
    #generate docx for each student
        cont = 0
        for aluno in json_alunos:
            cont  += 1
            # Load DOCX template from memory
            doc_io= io.BytesIO(template_bytes)
            doc = DocxTemplate(doc_io)
            doc.render(aluno)

            # Save the filled DOCX in memory
            doc_filled_io = io.BytesIO()
            doc.save(doc_filled_io)
            doc_filled_io.seek(0)
            
            # Add DOCX to ZIP file
            zipf.writestr(f"{aluno["Matricula"]}_documento.docx", doc_filled_io.read())
            #zipf.writestr(f"{aluno['Nome'].replace(' ', '_')}.docx", doc_filled_io.read())
    zip_io.seek(0)
    zip_content = zip_io.getvalue()
    return zip_content