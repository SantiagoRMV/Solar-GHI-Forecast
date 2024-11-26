# Cloud_Forecasting_CNN_LSTM

Este proyecto contiene el código necesario para la descarga, procesamiento y predicción de datos relacionados con la irradiación solar utilizando imágenes satelitales del producto ACMF del satélite GOES-16. El modelo integra redes neuronales convolucionales (CNN) y redes LSTM para la predicción de valores de irradiación a corto plazo.

## Introducción

El satélite GOES-16, parte de la serie GOES-R de la NOAA, proporciona datos meteorológicos avanzados. Este proyecto se enfoca en el producto **Advanced Baseline Imager Cloud Mask (ACMF)** para determinar la cobertura, altura y fase de las nubes, información crítica para predecir la irradiación solar.

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

- **`data/`**: Carpeta destinada al almacenamiento de los datasets utilizados en el proyecto.
- **`models/`**: Contiene los modelos entrenados y configuraciones de aprendizaje.
- **`notebooks/`**: Incluye los notebooks principales:
  - `NetCDF_Download.ipynb`: Descarga de archivos .nc del producto ACMF parametrizando fechas de interés.
  - `Image_Generator.ipynb`: Procesamiento de archivos .nc para generar imágenes y visualizar la metadata.
  - Otros notebooks auxiliares para procesamiento y análisis.
- **`reports/`**: Resultados y visualizaciones generadas durante el análisis y validación.
- **`src/`**: Código fuente para la implementación de modelos y utilidades.

## Resultados

1. **Modelo CNN-LSTM**:
   - Genera predicciones de irradiación para intervalos de tiempo de 10 minutos hacia adelante.
   - Entrenado utilizando imágenes del producto ACMF procesadas en `Image_Generator.ipynb`.

2. **Comparación con Prophet**:
   - Se realizó un análisis comparativo entre este modelo y el algoritmo Prophet de Meta, destacando la precisión y robustez de nuestro enfoque para predicciones basadas en imágenes.

3. **Visualización de Predicciones**:
   - Predicciones del modelo visualizadas en mapas e imágenes para evaluar el comportamiento en diferentes condiciones meteorológicas.

## Créditos y Reconocimientos

- **Datos**: Producto ACMF del satélite GOES-16 proporcionado por la NOAA.
- **Herramientas utilizadas**:
  - Bibliotecas de Python como TensorFlow, NumPy, Matplotlib, entre otras.
- **Contribuciones**: Desarrollo completo del modelo y análisis realizado por Juan Camilo Guavita y German Santiago Romero.
