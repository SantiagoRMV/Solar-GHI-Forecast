import os
import pandas as pd

def cargar_datos_generacion(directorio, columna_objetivo):
    """
    Carga los datos de generación desde archivos .csv en un directorio, totaliza los valores por hora,
    los convierte a kW y los organiza por fecha.
    Args:
        directorio (str): Ruta al directorio que contiene los archivos .csv.
        columna_objetivo (str): Nombre de la columna que contiene los datos de generación en W.
    Returns:
        dict: Diccionario con la fecha como clave y una lista de valores horarios en kW como valor.
    """
    datos = {}
    archivos_csv = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.csv')]

    for archivo in archivos_csv:
        try:
            print(f"Procesando archivo: {archivo}")
            # Leer el archivo
            df = pd.read_csv(os.path.join(directorio, archivo))

            # Validar columnas necesarias
            if columna_objetivo not in df.columns or 'Unnamed: 0' not in df.columns:
                print(f"Advertencia: {archivo} no contiene las columnas necesarias ('{columna_objetivo}', 'Unnamed: 0').")
                continue

            # Convertir a datetime
            df['Timestamp'] = pd.to_datetime(df['Unnamed: 0'])

            # Crear columna para las horas
            df['Hour'] = df['Timestamp'].dt.hour

            # Filtrar valores válidos
            df_validos = df[df[columna_objetivo].notna() & (df[columna_objetivo] > 0)]

            # Totalizar por hora y convertir a kW
            valores_por_hora = (
                df_validos.groupby('Hour')[columna_objetivo]
                .sum()
                .reindex(range(24), fill_value=0)  # Asegurar 24 horas
                .div(1000)  # Conversión de W a kW
                .tolist()
            )

            # Extraer fecha del archivo
            fecha_dd_mm = archivo.split('_')[-2] + '_' + archivo.split('_')[-1].replace('.csv', '')
            dia, mes = fecha_dd_mm.split('_')
            fecha = f"2023-{mes.zfill(2)}-{dia.zfill(2)}"

            # Guardar valores
            datos[fecha] = valores_por_hora

        except Exception as e:
            print(f"Error procesando el archivo {archivo}: {e}")
            continue

    return datos
