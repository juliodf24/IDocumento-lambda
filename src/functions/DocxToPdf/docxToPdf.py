from docx2pdf import convert
import os
# so funciona se tiver word
def docxToPdf(documents_path):
    final_path = documents_path[0]
    print(documents_path)
    for document_path in documents_path[1:]:
        docx_path = os.path.join(final_path, document_path + '.docx')
        pdf_path = os.path.join(final_path, document_path + '.pdf')
        convert( docx_path, pdf_path )
        os.remove(os.path.join(final_path, docx_path))
    return final_path
