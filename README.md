# 📊 Data Visualization Suite: Matplotlib vs. Seaborn vs. Streamlit

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pruebas-graficas-python-m49xqxuggor3ng2qddhr7s.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13+-4c72b0?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

> 🌐 **Demo en Vivo (Streamlit Cloud):** Puedes interactuar con la aplicación desplegada sin instalar nada directamente en:  
> **👉 [https://pruebas-graficas-python-m49xqxuggor3ng2qddhr7s.streamlit.app/](https://pruebas-graficas-python-m49xqxuggor3ng2qddhr7s.streamlit.app/)**

Una suite didáctica y comparativa que implementa **5 visualizaciones estadísticas fundamentales y accesibles**. El proyecto permite entender las diferencias arquitectónicas, sintácticas y estéticas entre **Matplotlib** (control granular de bajo nivel) y **Seaborn** (estadística de alto nivel orientada a DataFrames), desplegando todo de forma interactiva a través de una aplicación web construida con **Streamlit**.

---

## 📑 Tabla de Contenidos

- [🌐 Demo en Vivo](#-demo-en-vivo-streamlit-cloud)
- [🎯 Los 5 Gráficos Seleccionados](#-los-5-gráficos-seleccionados)
- [⚖️ Tabla Comparativa de Sintaxis](#️-tabla-comparativa-de-sintaxis)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Requisitos e Instalación](#️-requisitos-e-instalación)
- [🚀 Guía de Uso](#-guía-de-uso)
  - [1. Cuaderno Jupyter (`cuaderno_graficos.ipynb`)](#1-cuaderno-jupyter-cuaderno_graficosipynb)
  - [2. Dashboard Interactivo con Streamlit (`app.py`)](#2-dashboard-interactivo-con-streamlit-apppy)
- [🧠 Matplotlib vs. Seaborn: ¿Cuándo usar cada uno?](#-matplotlib-vs-seaborn-cuándo-usar-cada-uno)
- [📦 Dataset de Ejemplo](#-dataset-de-ejemplo)

---

## 🎯 Los 5 Gráficos Seleccionados

Se eligieron cinco tipos de gráficos estándar, fáciles de interpretar y de alta relevancia en análisis exploratorio de datos (EDA):

### 1. 📈 Gráfico de Líneas (*Line Plot*)
* **Propósito:** Analizar la evolución y patrones temporales de una variable continua.
* **Caso de uso:** Tendencia del volumen de ventas mensuales a lo largo de un año.
* **Puntos clave:** Conexión secuencial ordenada, marcadores de puntos clave y rejilla de apoyo.

### 2. 📊 Gráfico de Barras (*Bar Plot*)
* **Propósito:** Comparar una métrica numérica agregada (suma, conteo o promedio) a través de categorías cualitativas discretas.
* **Caso de uso:** Ventas acumuladas totales según la categoría del producto (Electrónica, Ropa, Hogar, etc.).
* **Puntos clave:** Ordenación por magnitud para facilitar la lectura inmediata.

### 3. 🔔 Histograma con Densidad (*Histogram & KDE*)
* **Propósito:** Examinar la distribución de frecuencias, simetría, sesgo y concentración de una variable cuantitativa continua.
* **Caso de uso:** Distribución de las puntuaciones de satisfacción reportadas por clientes (rango 1 a 10).
* **Puntos clave:** Configuración de intervalos (*bins*) y curva continua de densidad estimada (*Kernel Density Estimation*).

### 4. 🔵 Gráfico de Dispersión (*Scatter Plot*)
* **Propósito:** Evaluar la relación, fuerza y sentido de la correlación entre dos variables numéricas independientes.
* **Caso de uso:** Inversión en campañas publicitarias vs. Ventas generadas, segmentadas visualmente por categoría.
* **Puntos clave:** Detección de patrones lineales y heterocedasticidad.

### 5. 📦 Diagrama de Cajas (*Box Plot*)
* **Propósito:** Resumir la distribución estadística mediante los 5 números clave de Tukey (mínimo, $Q_1$, mediana, $Q_3$, máximo) e identificar valores atípicos (*outliers*).
* **Caso de uso:** Dispersión del valor de las ventas según el método de pago utilizado (Tarjeta, Efectivo, Transferencia).
* **Puntos clave:** Comparativa robusta no paramétrica inmune a extremos.

---

## ⚖️ Tabla Comparativa de Sintaxis

| Gráfico | Matplotlib (API Orientada a Objetos) | Seaborn (Orientada a DataFrames) |
|---|---|---|
| **Líneas** | `ax.plot(x, y, marker='o', color='...')` | `sns.lineplot(data=df, x='X', y='Y', ax=ax)` |
| **Barras** | `ax.bar(categorias, valores, color='...')` | `sns.barplot(data=df, x='Cat', y='Val', estimator=sum, ax=ax)` |
| **Histograma** | `ax.hist(df['col'], bins=10, edgecolor='black')` | `sns.histplot(data=df, x='col', bins=10, kde=True, ax=ax)` |
| **Dispersión** | `ax.scatter(df['x'], df['y'], alpha=0.7)` | `sns.scatterplot(data=df, x='x', y='y', hue='cat', ax=ax)` |
| **Cajas** | `ax.boxplot(datos_por_grupo, tick_labels=grupos)` | `sns.boxplot(data=df, x='grupo', y='val', ax=ax)` |

---

## 📁 Estructura del Proyecto

```text
PruebasGraficas/
├── cuaderno_graficos.ipynb   # Cuaderno Jupyter con los 10 gráficos pre-ejecutados
├── app.py                    # Aplicación web interactiva en Streamlit
├── requirements.txt          # Dependencias y librerías del proyecto
├── generar_cuaderno.py       # Script generador automatizado del notebook
└── README.md                 # Documentación completa y manual de usuario
```

---

## ⚙️ Requisitos e Instalación

### 1. Clonar o acceder al directorio del proyecto:
```bash
cd c:\Users\pacol\Desktop\PruebasGraficas
```

### 2. (Opcional pero recomendado) Crear un entorno virtual:
```bash
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En Windows (CMD):
.\venv\Scripts\activate.bat
```

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## 🚀 Guía de Uso

### 1. Cuaderno Jupyter (`cuaderno_graficos.ipynb`)

El cuaderno contiene la explicación paso a paso y el código reproducible. **Ya incluye todas las figuras renderizadas** para visualización directa en VSCode, GitHub o JupyterLab.

Para ejecutarlo interactivamente:
```bash
jupyter notebook cuaderno_graficos.ipynb
```

**Estructura del Notebook:**
1. **Paso 0:** Configuración de librerías y generación de datos sintéticos controlados con `numpy.random.seed(42)`.
2. **Parte 1 (Matplotlib):** Implementación manual, diseño de ejes (`fig, ax`), rejillas y leyendas.
3. **Parte 2 (Seaborn):** Misma serie de gráficos aprovechando el mapeo declarativo por columnas (`x`, `y`, `hue`, `palette`).
4. **Resumen y tabla de referencia.**

---

### 2. Dashboard Interactivo con Streamlit (`app.py`)

#### ☁️ Acceso Online Inmediato (Sin instalación previa)
Puedes probar la aplicación directamente en la nube sin necesidad de configurar Python en tu equipo:
> 🚀 **[Acceder a la Web en Streamlit Cloud](https://pruebas-graficas-python-m49xqxuggor3ng2qddhr7s.streamlit.app/)**

---

#### 💻 Ejecución en Local
Para lanzar el servidor web local con una interfaz gráfica moderna:

```bash
streamlit run app.py
```

Una vez ejecutado, abre tu navegador en `http://localhost:8501`.

#### 🎛️ Características de la Aplicación:
* **Modos de Visualización:**
  * ⚖️ **Comparación Lado a Lado:** Muestra ambas librerías en columnas paralelas para apreciar las diferencias de diseño al instante.
  * 🟦 **Solo Matplotlib:** Vista centrada en el renderizado clásico.
  * 🟧 **Solo Seaborn:** Vista con paletas temáticas y curvas de densidad estadísticas.
  * 🎯 **Gráfico a Gráfico:** Navegación por pestañas (*tabs*) para estudiar a fondo una visualización concreta.
* **Interactividad en tiempo real:**
  * *Slider* para ajustar el tamaño muestral ($N = 50$ a $500$ registros).
  * *Slider* para cambiar el número de barras (*bins*) del histograma.
  * Selector de paletas de color para Seaborn (`Blues_d`, `viridis`, `Set2`, `rocket`, `mako`).
  * Checkbox para inspeccionar la tabla de datos subyacente.
  * Tarjetas con indicadores métricos clave (*KPIs* de ventas y satisfacción).

---

## 🧠 Matplotlib vs. Seaborn: ¿Cuándo usar cada uno?

```
                     ┌────────────────────────────────────────┐
                     │          ¿Qué necesitas hacer?         │
                     └───────────────────┬────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   [Análisis rápido / EDA]                      [Control visual milimétrico / Custom UI]
   • Gráficos estadísticos directos             • Diagramas multipanel muy personalizados
   • Agrupaciones con `hue` automático          • Subplots con geometrías no estándar
   • Paletas y estilos listos                   • Anotaciones complejas en coordenadas
                 │                                               │
                 ▼                                               ▼
        Usa  S E A B O R N                             Usa  M A T P L O T L I B
```

* **Matplotlib:** Es el motor base. Ofrece control absoluto sobre cada píxel, línea, borde y texto de la figura. Ideal cuando requieres una personalización que ninguna otra librería ofrece o necesitas diagramar figuras complejas para publicaciones científicas.
* **Seaborn:** Es una capa de abstracción construida sobre Matplotlib. Diseñada para trabajar de forma nativa con DataFrames de Pandas, realiza agregaciones estadísticas automáticamente (medias, intervalos de confianza, densidades KDE) y produce gráficos con estética limpia y moderna escribiendo considerablemente menos líneas de código.

---

## 📦 Dataset de Ejemplo

Los datos se generan sintéticamente para garantizar que el proyecto funcione de inmediato **sin necesidad de descargas externas ni dependencias de internet**:

| Variable | Tipo | Descripción |
|---|---|---|
| `Mes` | Categórico temporal | Meses del año (`Ene` a `Dic`) |
| `Categoria` | Categórico | Rama de producto (`Electrónica`, `Ropa`, `Hogar`, etc.) |
| `Ventas` | Numérico continuo | Monto facturado (en miles de €) |
| `Publicidad` | Numérico continuo | Presupuesto invertido en marketing |
| `Satisfaccion` | Numérico (1 - 10) | Puntuación de experiencia del cliente |
| `Metodo_Pago` | Categórico | `Tarjeta`, `Efectivo` o `Transferencia` |
