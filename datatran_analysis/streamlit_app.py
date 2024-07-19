import pandas as pd
import streamlit as st

st.set_page_config(
    page_title='Análise de Acidentes de Trânsito',
    initial_sidebar_state='expanded',
    layout='wide',
    page_icon='🚓',
)

with st.sidebar:

    uploaded_csv = st.file_uploader(
        'A',
        type='csv',
    )

    if not uploaded_csv:

        st.warning(
            'Por favor, faça o upload do seu arquivo .csv para continuar.',
            icon='⚠️',
        )
    else:
        st.success('Arquivo carregado com sucesso!', icon='🎉')

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
    data = pd.read_csv(uploaded_csv, sep=';', encoding='latin1')
    st.write('# Sobre esse projeto')
    st.write(
        'Este é um projeto de análise de dados disponibilizados pela :red[Polícia Rodoviária Federal (PRF)]. O objetivo é analisar e visualizar informações sobre acidentes de trânsito ocorridos em rodovias federais brasileiras. Para isso, utilizei a linguagem de programação :red[Python], as bibliotecas :red[Pandas] e :red[Potly] para desenvolvimento das análises e criação dos gráficos e o :red[Streamlit] para organização do dashboard.'
    )
    st.write(
        'Escolhi esse dataset pois acredito que a análise de acidentes de trânsito é uma forma de :red[conscientizar] a população sobre a importância da segurança no trânsito e de incentivar ações que visem a redução de acidentes e mortes nas rodovias brasileiras. Além disso, a análise desses dados pode contribuir para a elaboração de :red[políticas públicas] e ações de fiscalização que visem a redução de acidentes e mortes no trânsito.'
    )

    st.write('## Apresentando o dataset')

    st.write(
        'Depois de selecionarmos as colunas que serão utilizadas na análise, o dataset ficou assim:'
    )
    data.fillna('Não informado', inplace=True)
    data.drop(
        columns=[
            'id',
            'horario',
            'km',
            'sentido_via',
            'tracado_via',
            'uso_solo',
            'regional',
            'delegacia',
            'uop',
        ],
        inplace=True,
    )

    st.dataframe(data.head(10))
    st.write('Nele já podemos ver algumas informações sobre os acidentes, como a :red[data], o :red[dia da semana], o :red[município], a :red[causa do acidente], o :red[tipo de acidente], o :red[tipo de veículo], a :red[quantidade de feridos e mortos], entre outras informações.')
    st.divider()
    st.write('## Dicionário de variáveis')
    st.write('A seguir, temos a descrição de cada variável do dataset:')
    st.write('**br**: Número da rodovia')
