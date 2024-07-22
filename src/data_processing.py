import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    # Remover duplicatas
    data = data.drop_duplicates()
    
    # Converter tipos de dados (exemplo: coluna de datas)
    if 'date_column' in data.columns:
        data['date_column'] = pd.to_datetime(data['date_column'])
    
    # Preencher valores ausentes (exemplo: preencher com a média)
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data[column].fillna(data[column].mean(), inplace=True)
    
    # Remover linhas com valores ausentes restantes
    data = data.dropna()
    
    # Tratamento de anomalias específicas (exemplo: valores negativos em colunas que devem ser positivas)
    if 'consumption' in data.columns:
        data = data[data['consumption'] >= 0]
    
    return data

if __name__ == "__main__":
    data = load_data('data/energy_consumption.csv')
    clean_data = clean_data(data)
    clean_data.to_csv('data/clean_energy_consumption.csv', index=False)
