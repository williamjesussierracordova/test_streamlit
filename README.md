# test_streamlit

Este repositorio contiene una aplicación de analítica académica construida con Streamlit. Funciona como un panel de control integral para la **"Universidad Nuevo Horizonte"**, permitiendo monitorear el rendimiento estudiantil, rastrear tasas de deserción y analizar datos de cursos. La aplicación se conecta a una base de datos MongoDB para extraer y visualizar analíticas en tiempo real a través de una serie de dashboards interactivos.

## Características

La aplicación está estructurada como un dashboard multipágina con una barra lateral de navegación central.

### 🏠 Página Principal
- Interfaz de bienvenida con tarjetas de acceso rápido para navegar a los distintos paneles analíticos.
- Visualización de métricas a nivel de sistema, como el número de dashboards activos y la fuente de datos.

### 📉 Dashboard de Deserción Estudiantil (`Vista_Desercion_Estudiantil.py`)
- **Indicadores Clave**: Seguimiento del total de estudiantes, número de deserciones y desglose por motivos financieros o académicos.
- **Análisis de Tendencias**: Visualización de las tasas de deserción a lo largo de diferentes periodos académicos y por causa.
- **Análisis Comparativo**: Comparación de calificaciones finales, asistencia y estado de pagos entre estudiantes activos y desertores mediante diagramas de caja (box plots) y gráficos de barras apiladas.
- **Interacción con el LMS**: Análisis y comparación de la actividad (inicios de sesión, vistas de contenido, entregas) en el Learning Management System.
- **Sistema de Alerta Temprana**: Identificación de estudiantes con alto riesgo de deserción basado en un modelo de puntuación que considera notas, asistencia y pagos atrasados.

### 🧑‍🎓 Perfil Estudiantil 360° (`Vista_Estudiante.py`)
- **Búsqueda Individual**: Permite buscar a un estudiante específico mediante su ID.
- **KPIs Integrales**: Muestra métricas clave del estudiante seleccionado, incluyendo el promedio ponderado acumulado, asistencia promedio y número de pagos pendientes.
- **Evaluación de Riesgo**: Muestra una alerta indicando si el estudiante está en riesgo de deserción y el motivo principal.
- **Visualización de Rendimiento**: Gráficos de promedio de notas por curso y desglose de tipos de actividad en el LMS.
- **Historial Financiero**: Tabla detallada del historial de pagos, incluyendo montos, fechas y estados (Pagado, Atrasado, Pendiente).

### 📚 Dashboard de Rendimiento de Cursos (`Vista_Cursos.py`)
- **Vista Centrada en el Curso**: Selección de cursos específicos para analizar su desempeño.
- **Métricas Agregadas**: KPIs del curso seleccionado, incluyendo inscritos, promedio de notas, tasa de aprobación y asistencia media.
- **Filtros Interactivos**: Capacidad de filtrar el análisis por periodo académico y rangos de calificación.
- **Visualización de Datos**: Histograma de distribución de notas y gráfico de dispersión que relaciona la asistencia con la calificación final.
- **Lista de Estudiantes**: Tabla paginada de estudiantes inscritos con sus respectivas notas finales y porcentajes de asistencia.

## Stack Tecnológico

- **Frontend**: Streamlit
- **Manipulación de Datos**: Python, Pandas
- **Base de Datos**: MongoDB (vía `pymongo`)
- **Visualización de Datos**: Plotly

## Guía de Inicio

Siga estas instrucciones para configurar y ejecutar el proyecto localmente.

### Prerrequisitos

- Python 3.8+
- Acceso a una instancia de MongoDB con la estructura de datos requerida.

### Instalación

1.  **Clonar el repositorio:**
    ```sh
    git clone [https://github.com/williamjesussierracordova/test_streamlit.git](https://github.com/williamjesussierracordova/test_streamlit.git)
    cd test_streamlit
    ```

2.  **Instalar los paquetes de Python necesarios:**
    ```sh
    pip install -r requirements.txt
    ```

### Configuración

La aplicación se conecta a MongoDB utilizando la gestión de secretos de Streamlit.

1.  Cree un archivo llamado `secrets.toml` dentro de un directorio `.streamlit` en la raíz de su proyecto:
    ```text
    .
    ├── .streamlit/
    │   └── secrets.toml
    └── App.py
    ...
    ```

2.  Agregue los detalles de conexión de su MongoDB en el archivo `secrets.toml`. El código espera un URI y un nombre de base de datos opcional.

    ```toml
    # .streamlit/secrets.toml
    [mongo]
    uri = "mongodb+srv://<usuario>:<password>@<cluster-url>/<db-name>?retryWrites=true&w=majority"
    db = "universidad_horizonte"
    ```

### Ejecución de la Aplicación

Inicie la app de Streamlit desde su terminal:
```sh
streamlit run App.py
```
La aplicación estará disponible en http://localhost:8501.

## Estructura del Proyecto

```
└── test_streamlit/
    ├── App.py                          # Enrutador principal y página de inicio
    ├── Vista_Cursos.py                 # Dashboard de análisis de rendimiento por curso
    ├── Vista_Desercion_Estudiantil.py  # Dashboard de análisis de deserción
    ├── Vista_Estudiante.py             # Dashboard de perfil 360° del estudiante
    ├── requirements.txt                # Dependencias del proyecto
    └── README.md                       # Este archivo
    └── README.md                       # This file
