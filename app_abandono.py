from codigo_desarrollo import *
import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
     page_title='Employee Retention Analyzer',
     page_icon='imagen_abandono.jpg',
     layout='wide')

# SIDEBAR
with st.sidebar:
    st.image('imagen_abandono.jpg')

    # INPUTS DE LA APLICACIÓN
    educacion = st.selectbox('Education', ['University', 'High School', 'Master', 'Primary'])
    carrera = st.selectbox('Career', ['Life Sciences', 'Medical', 'Other', 'Marketing', 'Technical Degree', 'Human Resources'])
    departamento = st.selectbox('Department', ['Research & Development', 'Sales', 'Human Resources'])
    puesto = st.selectbox('Position', ['Research Scientist', 'Laboratory Technician', 'Manufacturing Director', 'Healthcare Representative', 'Research Director', 'Manager', 'Sales Representative', 'Sales Executive', 'Human Resources'])
    anos_experiencia = st.number_input('Years of experience', 0, 25)
    edad = st.number_input('Age', 18, 65)
    estado_civil = st.selectbox('Marital status', ['Married', 'Single', 'Divorced'])
    horas_extra = st.radio('Overtime', ['Yes', 'No'])
    satisfaccion_companeros = st.selectbox('Satisfaction with Coworkers', ['Very_High', 'High', 'Medium', 'Low'])
    viajes = st.selectbox('Business trips', ['Travel_Frequently', 'Travel_Rarely', 'Non-Travel'])

    # DATOS CONOCIDOS (fijadas como datos estáticos por simplicidad)
    anos_con_manager_actual = 4
    evaluacion = 'Alta'
    nivel_acciones = 0
    nivel_laboral = 2
    num_empresas_anteriores = 2

# FUNCION PARA DETERMINAR EL COLOR DEL TEXTO
def get_color_for_value(value):
    if value <= 30:  # Bajo riesgo
        return "#00FF00"  # Verde
    elif value <= 70:  # Riesgo medio
        return "#FFCC00"  # Amarillo
    else:  # Alto riesgo
        return "#FF0000"  # Rojo

# MAIN
st.title('EMPLOYEE RETENTION ANALYZER')

# CALCULAR

# Crear el registro
registro = pd.DataFrame({'anos_con_manager_actual': anos_con_manager_actual,
                         'anos_experiencia': anos_experiencia,
                         'carrera': carrera,
                         'departamento': departamento,
                         'edad': edad,
                         'educacion': educacion,
                         'estado_civil': estado_civil,
                         'evaluacion': evaluacion,
                         'horas_extra': horas_extra,
                         'nivel_acciones': nivel_acciones,
                         'nivel_laboral': nivel_laboral,
                         'num_empresas_anteriores': num_empresas_anteriores,
                         'puesto': puesto,
                         'satisfaccion_companeros': satisfaccion_companeros,
                         'viajes': viajes},
                        index=[0])
# Cambiar el nombre del índice
registro.index.name = 'id'

# CALCULAR RIESGO
if st.sidebar.button('CALCULATE PROBABILITY OF ATTRITION'):
    st.write('Designed and Powered by Álvaro Gamundi')
    # Ejecutar el scoring
    Pobabilidad = ejecutar_modelos(registro)

    # Mostrar la probabilidad
    probabilidad_value = Pobabilidad[0]  # Asumimos que Pobabilidad es un array
    st.write('The expected probability of job turnover is:')
    st.metric(label="EXPECTED PROBABILITY", value=f"{Pobabilidad[0]}%")

    # Crear gráfico de tipo gauge (velocímetro)
    gauge_options = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Employee Turnover Risk",
                "type": "gauge",
                "radius": "99%",  # Aumentamos el tamaño de la esfera
                "center": ["50%", "50%"],  # Centrado en la pantalla
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                        "color": [
                            [0.3, "#00FF00"],  # Bajo: Verde
                            [0.7, "#FFCC00"],  # Medio: Amarillo
                            [1, "#FF0000"],  # Alto: Rojo
                        ],
                    },
                },
                "progress": {"show": False},  # Desactivamos el progreso (la barra azul)
                "detail": {
                    "valueAnimation": "true", 
                    "formatter": "{value}%",
                    "fontSize": 18,  # Tamaño de letra más grande para el valor
                    "color": get_color_for_value(probabilidad_value),  # Función para color dinámico del texto
                },
                "title": {
                    "show": True,
                    "fontSize": 18,  # Tamaño de letra para el nombre
                },
                "data": [{"value": probabilidad_value, "name": "Turnover Probability"}],
            }
        ],
    }

    # Mostrar el gráfico en la app
    st_echarts(options=gauge_options, width="100%", key="turnover_gauge")

else:
    st.write('DEFINE THE WORKER PARAMETERS AND CLICK ON CALCULATE')
    st.write('Designed and Powered by Álvaro Gamundi')


    