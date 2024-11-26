import pandas as pd
from pydataxm.pydatasimem import ReadSIMEM

def procesar_precio_bolsa(simem, p_bolsa_id, fecha_inicial, fecha_final):
    """
    Procesa los datos de PrecioBolsa para un rango de fechas y genera una lista por día con 24 valores horarios.
    Args:
        simem (ReadSIMEM): Objeto SIMEM para obtener datos.
        p_bolsa_id (str): ID de la variable PrecioBolsa.
        fecha_inicial (str): Fecha inicial en formato 'YYYY-MM-DD'.
        fecha_final (str): Fecha final en formato 'YYYY-MM-DD'.
    Returns:
        dict: Diccionario con la fecha como clave y una lista de valores horarios redondeados como valor.
    """
    rango_fechas = pd.date_range(start=fecha_inicial, end=fecha_final)
    resultados_por_dia = {}

    for fecha in rango_fechas:
        fecha_str = fecha.strftime('%Y-%m-%d')
        try:
            p_bolsa_df = simem.main(p_bolsa_id, fecha_str, fecha_str)

            filtro_bolsa = 'PB_Nal'
            p_bolsa_df_filtrado: pd.DataFrame = (
                p_bolsa_df[p_bolsa_df['CodigoVariable'] == filtro_bolsa]
                .copy()
                .sort_values('FechaHora')
                .reset_index()
            )
            p_bolsa_df_filtrado['FechaHora'] = pd.to_datetime(p_bolsa_df_filtrado['FechaHora'], format='%Y-%m-%d %H:%M:%S')
            p_bolsa_df_filtrado['Fecha'] = p_bolsa_df_filtrado['FechaHora'].dt.strftime('%Y-%m-%d')
            p_bolsa_df_filtrado['Hour'] = p_bolsa_df_filtrado['FechaHora'].dt.strftime('%H:%M:%S')
            p_bolsa_df_filtrado.rename(columns={'Valor': 'PrecioBolsa'}, inplace=True)
            p_bolsa_df_filtrado = (
                p_bolsa_df_filtrado[['Fecha', 'Hour', 'PrecioBolsa']]
                .groupby(['Fecha', 'Hour'])
                .mean()
                .reset_index()
            )
            p_bolsa_df_filtrado['PrecioBolsa'] = p_bolsa_df_filtrado['PrecioBolsa'].round(0)
            valores_horarios = p_bolsa_df_filtrado['PrecioBolsa'].tolist()
            if len(valores_horarios) == 24:
                resultados_por_dia[fecha_str] = valores_horarios
            else:
                print(f"Advertencia: {fecha_str} tiene {len(valores_horarios)} registros en lugar de 24.")
        except Exception as e:
            print(f"Error procesando la fecha {fecha_str}: {e}")
            continue

    return resultados_por_dia

if __name__ == "__main__":
    simem = ReadSIMEM()
    p_bolsa_id = 'EC6945'
    fecha_inicial = '2023-04-01'
    fecha_final = '2023-04-05'

    resultados = procesar_precio_bolsa(simem, p_bolsa_id, fecha_inicial, fecha_final)
    print(resultados)
