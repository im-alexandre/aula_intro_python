#!/usr/bin/env python
import pandas as pd

# importação das bases
df_train = pd.read_excel('dados.xls',
                         sheet_name='Training_Data', usecols=['STG', 'SCG', 'STR', 'LPR', 'PEG', ' UNS'])


df_test = pd.read_excel('dados.xls',
                         sheet_name='Test_Data', usecols=['STG', 'SCG', 'STR', 'LPR', 'PEG', ' UNS'])

df_full = pd.concat([df_train, df_test])

def arredonda(numero: float) -> float:
    arredondado = round(numero, 2)

def remove_espacos(dado: str) -> str:
    minusculo = dado.lower()
    sem_espaco = minusculo.replace(' ', '_')
    return sem_espaco


def pre_process(dataframe, nome_dataset):
    """ Função de pré-processamento:
    sanitiza os valores do atributo alvo e salva o dataset em formatos '.csv' e '.arff' """
    dataframe['UNS'] = dataframe[' UNS'].apply(remove_espacos)
    dataframe.drop(columns=[' UNS'], inplace=True)
    dataframe.to_excel(f'{nome_dataset}.xlsx', index=False)
    return dataframe

# Trata e salva as bases
pre_process(df_train, 'dataset_train')
pre_process(df_test, 'dataset_test')
df_full = pre_process(df_full, 'dataset_full')


# Extrai as estatísticas descritivas da base completa e salva em excel
descricao = df_full.drop(columns=['UNS']).describe()
descricao.columns = ["Valores", "STG", "SCG", "STR", "LPR"]
descricao.index = ["Número de instâncias", "Média", "Desvio Padrão",
                   "Mínimo", "Q1 (25%)", "Mediana (50%)", "Q3 (75%)", "Máximo"  ]
descricao.drop(columns=["Valores"], inplace=True)

descricao.applymap(arredonda).to_excel('estatisticas.xlsx')

