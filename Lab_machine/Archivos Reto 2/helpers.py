import pandas as pd
import os, glob

def check_requirements():
    route = glob.glob('*.csv')
    assert len(route) != 0, 'No hay archivos csv en la carpeta'
    print('Archivos encontrados:', route)
    try:
        handle = pd.read_csv("predictions.csv")
    except:
        raise ImportError('No se ha encontrado el archivo predictions.csv, revise si el nombre es correcto o si el archivo se exportó correctamente')
    
    print('Archivo cargado correctamente')

    if len(list(handle.columns)) < 2:
        raise ValueError('El archivo predictions.csv no tiene las columnas necesarias')
    print('Columnas encontradas')

    if "prediction" not in handle.columns:
        raise ValueError('El archivo predictions.csv no tiene la columna prediction')
    print('Columna prediction encontrada')
    if "data" not in handle.columns:
        raise ValueError('El archivo predictions.csv no tiene la columna data')
    
    print('Las columnas tienen el nombre correcto')
    if len(handle) == 0:
        raise ValueError('El archivo predictions.csv está vacío')
    
    print('El archivo predictions.csv no está vacío')
    
    if len(handle["prediction"]) != 2160:
        raise ValueError('El archivo predictions.csv no tiene la cantidad de predicciones correcta')
    
    print('La cantidad de predicciones es correcta')
    print('Requisitos completados')
    
