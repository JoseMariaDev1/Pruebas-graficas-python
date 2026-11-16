import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial de la página
st.set_page_config(
    page_title="Dashboard de Visualización de Gráficos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo personalizado simple
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .chart-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# Título y encabezado
st.markdown('<div class="main-title">📊 Visualización de 5 Gráficos Esenciales</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Demostración comparativa de gráficos estadísticos medianamente sencillos usando <b>Matplotlib</b>, <b>Seaborn</b> y <b>Streamlit</b>.</div>', unsafe_allow_html=True)

# Barra lateral (Sidebar)
st.sidebar.header("⚙️ Configuración y Filtros")

modo_vista = st.sidebar.radio(
    "Selecciona el modo de visualización:",
    ["⚖️ Comparación Lado a Lado", "🟦 Solo Matplotlib", "🟧 Solo Seaborn", "🎯 Gráfico a Gráfico"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Parámetros de Datos")
n_muestras = st.sidebar.slider("Número de transacciones simuladas:", min_value=50, max_value=500, value=200, step=25)
bins_hist = st.sidebar.slider("Número de barras (bins) en histograma:", min_value=5, max_value=25, value=10, step=1)
paleta_seaborn = st.sidebar.selectbox("Paleta de color (Seaborn):", ["Blues_d", "viridis", "Set2", "rocket", "mako"])

mostrar_datos = st.sidebar.checkbox("Mostrar tabla de datos simulados", value=False)

# Función con caché para generar datos reproducibles
@st.cache_data
def generar_datos(n):
    np.random.seed(42)
    # 1. Datos mensuales
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ventas_base = [18, 22, 25, 29, 35, 42, 48, 45, 38, 40, 52, 65]
    df_mensual = pd.DataFrame({'Mes': meses, 'Ventas': ventas_base})

    # 2. Transacciones individuales
    categorias = ['Electrónica', 'Ropa', 'Hogar', 'Libros', 'Deportes']
    metodos_pago = ['Tarjeta', 'Efectivo', 'Transferencia']

    df_trans = pd.DataFrame({
        'Categoria': np.random.choice(categorias, size=n, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        'Publicidad': np.random.uniform(2, 20, size=n),
        'Metodo_Pago': np.random.choice(metodos_pago, size=n, p=[0.6, 0.25, 0.15]),
        'Satisfaccion': np.clip(np.random.normal(loc=7.5, scale=1.3, size=n), 1, 10)
    })

    factor_cat = {'Electrónica': 15, 'Ropa': 10, 'Hogar': 8, 'Libros': 5, 'Deportes': 9}
    df_trans['Ventas'] = (df_trans['Publicidad'] * 1.8 + df_trans['Categoria'].map(factor_cat) + np.random.normal(0, 4, size=n)).round(2)
    df_trans['Satisfaccion'] = df_trans['Satisfaccion'].round(1)

    return df_mensual, df_trans

df_mensual, df = generar_datos(n_muestras)

# Métricas resumen en tarjetas
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric("Total Registros", f"{len(df):,}")
with col_m2:
    st.metric("Ventas Totales", f"{df['Ventas'].sum():,.2f} k€")
with col_m3:
    st.metric("Venta Promedio", f"{df['Ventas'].mean():.2f} k€")
with col_m4:
    st.metric("Satisfacción Media", f"{df['Satisfaccion'].mean():.1f} / 10")

if mostrar_datos:
    st.markdown("### 📋 Vista Previa del Conjunto de Datos")
    st.dataframe(df.head(15), use_container_width=True)

st.markdown("---")

# ==========================================
# FUNCIONES GENERADORAS DE LOS 5 GRÁFICOS
# ==========================================

# 1. Gráfico de Líneas
def plot_line_mpl():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df_mensual['Mes'], df_mensual['Ventas'], marker='o', color='#1f77b4', linewidth=2, markersize=5)
    ax.set_title('Evolución Mensual (Matplotlib)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Ventas (miles de €)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    return fig

def plot_line_sns():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df_mensual, x='Mes', y='Ventas', marker='o', ax=ax, color='#1f77b4', linewidth=2.5)
    ax.set_title('Evolución Mensual (Seaborn)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Ventas (miles de €)')
    plt.tight_layout()
    return fig

# 2. Gráfico de Barras
def plot_bar_mpl():
    ventas_cat = df.groupby('Categoria')['Ventas'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    colores = ['#4c72b0', '#55a868', '#c44e52', '#8172b3', '#ccb974']
    ax.bar(ventas_cat.index, ventas_cat.values, color=colores, edgecolor='black', alpha=0.85)
    ax.set_title('Ventas por Categoría (Matplotlib)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Categoría')
    ax.set_ylabel('Ventas Totales (miles de €)')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=15)
    plt.tight_layout()
    return fig

def plot_bar_sns():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=df, 
        x='Categoria', 
        y='Ventas', 
        estimator=np.sum, 
        errorbar=None, 
        palette=paleta_seaborn, 
        hue='Categoria', 
        legend=False,
        ax=ax
    )
    ax.set_title('Ventas por Categoría (Seaborn)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Categoría')
    ax.set_ylabel('Ventas Totales (miles de €)')
    plt.xticks(rotation=15)
    plt.tight_layout()
    return fig

# 3. Histograma
def plot_hist_mpl():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df['Satisfaccion'], bins=bins_hist, color='#2ca02c', edgecolor='black', alpha=0.7)
    ax.set_title('Satisfacción del Cliente (Matplotlib)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Puntuación (1-10)')
    ax.set_ylabel('Frecuencia')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    return fig

def plot_hist_sns():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(data=df, x='Satisfaccion', bins=bins_hist, kde=True, color='#2ca02c', ax=ax)
    ax.set_title('Satisfacción del Cliente con KDE (Seaborn)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Puntuación (1-10)')
    ax.set_ylabel('Frecuencia')
    plt.tight_layout()
    return fig

# 4. Dispersión (Scatter Plot)
def plot_scatter_mpl():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(df['Publicidad'], df['Ventas'], color='#d62728', alpha=0.65, edgecolors='black', s=45)
    ax.set_title('Publicidad vs. Ventas (Matplotlib)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Gasto Publicidad (miles €)')
    ax.set_ylabel('Ventas (miles €)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    return fig

def plot_scatter_sns():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(
        data=df, 
        x='Publicidad', 
        y='Ventas', 
        hue='Categoria', 
        palette='tab10', 
        s=60, 
        alpha=0.75, 
        ax=ax
    )
    ax.set_title('Publicidad vs. Ventas por Categoría (Seaborn)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Gasto Publicidad (miles €)')
    ax.set_ylabel('Ventas (miles €)')
    ax.legend(title='Categoría', fontsize=8, title_fontsize=9)
    plt.tight_layout()
    return fig

# 5. Diagrama de Cajas (Box Plot)
def plot_box_mpl():
    fig, ax = plt.subplots(figsize=(6, 4))
    metodos = df['Metodo_Pago'].unique()
    datos_box = [df[df['Metodo_Pago'] == m]['Ventas'].values for m in metodos]
    box = ax.boxplot(datos_box, tick_labels=metodos, patch_artist=True)
    colores_box = ['#a6cee3', '#b2df8a', '#fb9a99']
    for patch, color in zip(box['boxes'], colores_box):
        patch.set_facecolor(color)
        patch.set_alpha(0.8)
    ax.set_title('Ventas por Método de Pago (Matplotlib)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Método de Pago')
    ax.set_ylabel('Ventas (miles €)')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    return fig

def plot_box_sns():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(
        data=df, 
        x='Metodo_Pago', 
        y='Ventas', 
        hue='Metodo_Pago',
        palette='Set2', 
        legend=False,
        ax=ax
    )
    ax.set_title('Ventas por Método de Pago (Seaborn)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Método de Pago')
    ax.set_ylabel('Ventas (miles €)')
    plt.tight_layout()
    return fig


# Lista descriptiva de los 5 gráficos
charts_info = [
    {
        "num": 1,
        "nombre": "Gráfico de Líneas (Line Plot)",
        "desc": "Ideal para mostrar tendencias y variaciones continuas a lo largo de una serie temporal o secuencia ordenada.",
        "mpl": plot_line_mpl,
        "sns": plot_line_sns
    },
    {
        "num": 2,
        "nombre": "Gráfico de Barras (Bar Plot)",
        "desc": "Permite comparar métricas numéricas agregadas (sumas o medias) entre grupos o categorías discretas.",
        "mpl": plot_bar_mpl,
        "sns": plot_bar_sns
    },
    {
        "num": 3,
        "nombre": "Histograma (Histogram / Distribución)",
        "desc": "Muestra la frecuencia y distribución de una variable cuantitativa continua, revelando asimetría y concentración.",
        "mpl": plot_hist_mpl,
        "sns": plot_hist_sns
    },
    {
        "num": 4,
        "nombre": "Gráfico de Dispersión (Scatter Plot)",
        "desc": "Muestra la relación entre dos variables numéricas, permitiendo detectar correlaciones lineales, patrones o dispersión.",
        "mpl": plot_scatter_mpl,
        "sns": plot_scatter_sns
    },
    {
        "num": 5,
        "nombre": "Diagrama de Cajas (Box Plot)",
        "desc": "Resume la mediana, los cuartiles (Q1, Q3), el rango intercuartílico y posibles valores atípicos (outliers) por grupo.",
        "mpl": plot_box_mpl,
        "sns": plot_box_sns
    }
]

# ==========================================
# RENDERIZADO SEGÚN EL MODO ELEGIDO
# ==========================================

if modo_vista == "⚖️ Comparación Lado a Lado":
    for chart in charts_info:
        st.subheader(f"{chart['num']}. {chart['nombre']}")
        st.caption(chart['desc'])
        col_izq, col_der = st.columns(2)
        with col_izq:
            st.markdown("**Versión Matplotlib**")
            fig_mpl = chart['mpl']()
            st.pyplot(fig_mpl)
            plt.close(fig_mpl)
        with col_der:
            st.markdown("**Versión Seaborn**")
            fig_sns = chart['sns']()
            st.pyplot(fig_sns)
            plt.close(fig_sns)
        st.markdown("---")

elif modo_vista == "🟦 Solo Matplotlib":
    st.info("Mostrando los 5 gráficos generados exclusivamente con **Matplotlib**.")
    for chart in charts_info:
        st.subheader(f"{chart['num']}. {chart['nombre']}")
        st.caption(chart['desc'])
        col1, col2 = st.columns([3, 1])
        with col1:
            fig = chart['mpl']()
            st.pyplot(fig)
            plt.close(fig)
        with col2:
            st.markdown("""
            **Características en Matplotlib:**
            - Control explícito de la figura (`fig, ax`).
            - Asignación manual de etiquetas y rejillas (`grid`).
            - Mapeo manual de colores si se requiere.
            """)
        st.markdown("---")

elif modo_vista == "🟧 Solo Seaborn":
    st.info("Mostrando los 5 gráficos generados exclusivamente con **Seaborn**.")
    for chart in charts_info:
        st.subheader(f"{chart['num']}. {chart['nombre']}")
        st.caption(chart['desc'])
        col1, col2 = st.columns([3, 1])
        with col1:
            fig = chart['sns']()
            st.pyplot(fig)
            plt.close(fig)
        with col2:
            st.markdown("""
            **Características en Seaborn:**
            - Diseñado directamente para DataFrames de pandas.
            - Manejo automático de leyendas, paletas y agregaciones.
            - Soporte para curvas de densidad estimadas (KDE).
            """)
        st.markdown("---")

elif modo_vista == "🎯 Gráfico a Gráfico":
    opciones_graficos = [f"{c['num']}. {c['nombre']}" for c in charts_info]
    seleccionado = st.selectbox("Elige el gráfico que deseas examinar:", opciones_graficos)
    idx = int(seleccionado.split(".")[0]) - 1
    chart = charts_info[idx]

    st.markdown(f"### {chart['nombre']}")
    st.markdown(chart['desc'])

    tab_ambos, tab_mpl, tab_sns = st.tabs(["⚖️ Ambos Lado a Lado", "🟦 Solo Matplotlib", "🟧 Solo Seaborn"])
    
    with tab_ambos:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Matplotlib**")
            f1 = chart['mpl']()
            st.pyplot(f1)
            plt.close(f1)
        with c2:
            st.markdown("**Seaborn**")
            f2 = chart['sns']()
            st.pyplot(f2)
            plt.close(f2)

    with tab_mpl:
        f_mpl = chart['mpl']()
        st.pyplot(f_mpl)
        plt.close(f_mpl)

    with tab_sns:
        f_sns = chart['sns']()
        st.pyplot(f_sns)
        plt.close(f_sns)

st.markdown("💡 **Tip:** Puedes ejecutar esta aplicación localmente con el comando: `streamlit run app.py`")
