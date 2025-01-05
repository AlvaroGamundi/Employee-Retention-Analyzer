from codigo_desarrollo import *
import streamlit as st


#CONFIGURACION DE LA PÁGINA
st.set_page_config(
     page_title = 'Employee Retention Analyzer',
     page_icon = 'logo.jpg',
     layout = 'wide')


#SIDEBAR
with st.sidebar:
    st.image('logo_2.jpg')

    #INPUTS DE LA APLICACION
    educacion = st.selectbox('Education', ['Universitaria', 'Secundaria', 'Master', 'Primaria'])
    carrera = st.selectbox('Career', ['Life Sciences', 'Medical', 'Other', 'Marketing','Technical Degree', 'Human Resources'])
    departamento = st.selectbox('Department', ['Research & Development', 'Sales', 'Human Resources'])
    puesto=st.selectbox('Position', ['Research Scientist', 'Laboratory Technician','Manufacturing Director', 'Healthcare Representative','Research Director', 'Manager', 'Sales Representative','Sales Executive', 'Human Resources'])
    anos_experiencia = st.number_input('Years of experience', 0, 25)
    edad = st.number_input('Age', 18, 65)
    estado_civil = st.selectbox('Marital status', ['Married', 'Single', 'Divorced'])
    horas_extra = st.radio('Overtime', ['Yes', 'No'])
    satisfaccion_companeros=st.selectbox('Satisfaction with Coworkers', ['Very_High','High', 'Medium',  'Low'])
    viajes=st.selectbox('Business trips', ['Travel_Frequently', 'Travel_Rarely', 'Non-Travel'])


    #DATOS CONOCIDOS (fijadas como datos estaticos por simplicidad)
    anos_con_manager_actual = 4
    evaluacion='Alta'
    nivel_acciones=0
    nivel_laboral=2
    num_empresas_anteriores=2

#MAIN
st.title('EMPLOYEE RETENTION ANALYZER')

#CALCULAR

#Crear el registro
registro = pd.DataFrame({'anos_con_manager_actual':anos_con_manager_actual,
                        'anos_experiencia':anos_experiencia,
                        'carrera':carrera,
                        'departamento':departamento,
                        'edad':edad,
                        'educacion':educacion,
                        'estado_civil':estado_civil,
                        'evaluacion':evaluacion,
                        'horas_extra':horas_extra,
                        'nivel_acciones':nivel_acciones,
                        'nivel_laboral':nivel_laboral,
                        'num_empresas_anteriores':num_empresas_anteriores,
                        'puesto':puesto,
                        'satisfaccion_companeros':satisfaccion_companeros,
                        'viajes':viajes}
                        ,index=[0])
# Cambiar el nombre del índice
registro.index.name = 'id'



#CALCULAR RIESGO
if st.sidebar.button('CALCULATE PROBABILITY OF ATTRITION'):
    st.write('Designed and Powered by Álvaro Gamundi')
    #Ejecutar el scoring
    Pobabilidad = ejecutar_modelos(registro)


    st.write('The expected probability of job turnover is:')
    st.metric(label="EXPECTED PROBABILITY", value=f"{Pobabilidad[0]}%")

else:
    st.write('DEFINE THE WORKER PARAMETERS AND CLICK ON CALCULATE')
    st.write('Designed and Powered by Álvaro Gamundi')    
    