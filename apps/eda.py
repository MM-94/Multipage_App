import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    # Titolo dell'applicazione
    st.title('Analisi Esplorativa dei Dati')

    # Controlla se i dati sono presenti nello stato della sessione
    if 'df' in st.session_state:
        df = st.session_state['df']

        # Selezione delle colonne per il grafico a dispersione
        columns = df.columns.tolist()
        x_axis = st.sidebar.selectbox('Seleziona la variabile per l\'asse X', columns)
        y_axis = st.sidebar.selectbox('Seleziona la variabile per l\'asse Y', columns)

        if x_axis and y_axis:
            # Creazione dello scatterplot interattivo
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatterplot di {x_axis} vs {y_axis}', hover_data=df.columns)
            st.plotly_chart(fig)
    else:
        st.error("Nessun dato caricato. Per favore, carica un dataset nella sezione 'Data'.")
