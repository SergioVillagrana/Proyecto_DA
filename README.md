# Análisis de Vehículos en EE.UU.

Este proyecto es un dashboard interactivo construido con **Streamlit**, **Pandas** y **Plotly Express**, como parte del curso de análisis de datos.

La aplicación permite:
- Visualizar un histograma de la variable **odometer**.
- Construir un gráfico de dispersión entre **odometer** y **price**.
- Seleccionar estos gráficos mediante casillas de verificación.
- Interactuar con los datos de anuncios de venta de vehículos en EE.UU.

## Dataset

El conjunto de datos utilizado es **vehicles_us.csv**, el cual contiene información sobre anuncios de venta de coches en Estados Unidos.

## Cómo ejecutar la aplicación

1. Activa el entorno virtual:
    ```bash
    .\vehicles_env\Scripts\activate
    ```

2. Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```

La aplicación se abrirá automáticamente en tu navegador en:

(http://localhost:8501)


## Estructura del proyecto

Proyecto_DA/
│── app.py
│── vehicles_us.csv
│── requirements.txt
│── README.md
│── notebooks/
│ └── EDA.ipynb
└── vehicles_env/


## Funcionalidad

- **Gráficos interactivos** generados con Plotly.
- Interfaz simple e intuitiva con Streamlit.
- Opcional: selección de gráficos mediante checkboxes.

---
