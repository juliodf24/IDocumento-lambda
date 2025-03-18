import pandas as pd

def excel_para_json(file_path):
    print('gerando json do exel....')
    df = pd.read_excel(file_path)
    json_data = df.to_dict(orient='records')
    print('json do exel gerado com sucesso')
    # print(json_data)
    return json_data