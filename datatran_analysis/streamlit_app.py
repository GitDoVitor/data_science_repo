import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Análise de Acidentes de Trânsito',
    initial_sidebar_state='expanded',
    page_icon='🚓',
)

with st.sidebar:

    uploaded_csv = st.file_uploader(
        '',
        type='csv',
    )

    if not uploaded_csv:
        st.warning("Por favor, faça o upload do seu arquivo .csv para continuar.", icon="⚠️")
    else:
        st.success("Arquivo carregado com sucesso!", icon="🎉")

if not uploaded_csv:
    st.write(
        '<h1 style="font-size: 30px;">📥 Para começar, faça o upload de um arquivo .csv </h1>',
        unsafe_allow_html=True,
    )
    st.info(
        'Utilize um arquivo .csv de acidentes de trânsito disponível no site de [Dados Abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)',
        icon='ℹ️',
    )
else:
    data = pd.read_csv(
       uploaded_csv, sep=';', encoding='latin1'
    )
    st.write('## Sobre esse projeto')
    st.write(
        'Este é um projeto de análise de dados disponibilizados pela :red[Polícia Rodoviária Federal (PRF)]. O objetivo é analisar e visualizar informações sobre acidentes de trânsito ocorridos em rodovias federais brasileiras. Para isso, utilizei a linguagem de programação :red[Python], as bibliotecas :red[Pandas] e :red[Potly] para desenvolvimento das análises e criação dos gráficos e o :red[Streamlit] para organização do dashboard.'
    )
    