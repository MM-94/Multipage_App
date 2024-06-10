import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets

def app():
    st.title('Data')

    # Descrizione breve
    st.write("Carica un file Excel o CSV per visualizzare i dati.")

    # Caricamento del file nella sidebar
    st.sidebar.title("Caricamento File")
    uploaded_file = st.sidebar.file_uploader("Scegli un file", type=['csv', 'xlsx'])

    # Controlla se un file è stato caricato
    if uploaded_file is not None:
        try:
            # Se il file è un CSV
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            # Se il file è un Excel
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)

            # Memorizza il dataframe nello stato della sessione
            st.session_state['df'] = df
            
            # Mostra il dataframe caricato
            st.write("Ecco un'anteprima del dataset:")
            st.dataframe(df)

            # Mostra la tabella descrittiva generale
            st.write("Descrizione statistica del dataset:")
            st.dataframe(df.describe())

        except Exception as e:
            # Gestione degli errori
            st.error(f"Errore nel caricamento del file: {e}")

    elif 'df' in st.session_state:
        # Se il file è già stato caricato, mostra i dati memorizzati
        df = st.session_state['df']
        st.write("Ecco un'anteprima del dataset:")
        st.dataframe(df)

        st.write("Descrizione statistica del dataset:")
        st.dataframe(df.describe())
    else:
        # Messaggio da mostrare se nessun file è stato caricato
        st.sidebar.info("Per favore, carica un file per visualizzare i dati.")


