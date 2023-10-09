"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    cantidad_filas = tbl0.shape[0]
    return cantidad_filas

def pregunta_02():
    cantidad_columnas = tbl0.shape[1]
    return cantidad_columnas

def pregunta_03():
    cantidad_por_letra = tbl0['_c1'].value_counts().sort_index()
    return cantidad_por_letra

def pregunta_04():
    promedio_por_letra = tbl0.groupby('_c1')['_c2'].mean()
    return promedio_por_letra

def pregunta_05():
    maximo_por_letra = tbl0.groupby('_c1')['_c2'].max()
    return maximo_por_letra

def pregunta_06():
    valores_unicos = tbl1['_c4'].str.upper().unique()
    valores_unicos = sorted(valores_unicos)
    return valores_unicos

def pregunta_07():
    suma_por_letra = tbl0.groupby('_c1')['_c2'].sum()
    return suma_por_letra


def pregunta_08():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']
    return tbl0

def pregunta_09():
    df = pd.read_csv('tbl0.tsv', sep='\t')
    df['year'] = df['_c3'].str[:4]
    return df

def pregunta_10():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tabla_resultante = tbl0.groupby('_c1')['_c2'].agg(list).reset_index()
    tabla_resultante['_c2'] = tabla_resultante['_c2'].apply(lambda x: sorted(x))
    tabla_resultante['_c2'] = tabla_resultante['_c2'].apply(lambda x: ':'.join(map(str, x)))
    tabla_resultante.set_index('_c1', inplace=True)
    return tabla_resultante

def pregunta_11():
    tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
    tbl1 = tbl1.sort_values(by='_c4')
    tabla_resultante = tbl1.groupby('_c0')['_c4'].agg(','.join).reset_index()
    return tabla_resultante

def pregunta_12():
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
    tbl2 = tbl2.sort_values(by=['_c5a', '_c5b'])
    tbl2['_c5'] = tbl2['_c5a'].astype(str) + ':' + tbl2['_c5b'].astype(str)
    tabla_resultante = tbl2.groupby('_c0')['_c5'].agg(','.join).reset_index()
    return tabla_resultante

def pregunta_13():
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
    merged_df = tbl0.merge(tbl2, on='_c0')
    suma_por_c1 = merged_df.groupby('_c1')['_c5b'].sum()
    return suma_por_c1