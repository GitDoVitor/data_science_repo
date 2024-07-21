import pandas as pd
import streamlit as st
import io

st.set_page_config(
    page_title='Análise de Acidentes de Trânsito',
    initial_sidebar_state='expanded',
    layout='wide',
    page_icon='🚓',
    # TODO
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': 'https://www.google.com',
        'About': '# This is a header. This is an *extremely* cool app!',
    },
)

with st.sidebar:

    uploaded_csv = st.file_uploader(
        'Faça o upload do seu arquivo .csv',
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
    data = pd.read_csv(uploaded_csv, sep=';', encoding='latin1', decimal=',')
    st.write('# Sobre esse projeto')
    st.write(
        'Este é um projeto de análise de dados disponibilizados pela <span style="color: #FF6161">Polícia Rodoviária Federal (PRF)</span>. O objetivo é analisar e visualizar informações sobre acidentes de trânsito ocorridos em rodovias federais brasileiras. Para isso, utilizei a linguagem de programação <span style="color: #FF6161">Python</span>, as bibliotecas <span style="color: #FF6161">Pandas</span> e <span style="color: #FF6161">Potly</span> para desenvolvimento das análises e criação dos gráficos e o <span style="color: #FF6161">Streamlit</span> para organização do dashboard.',
        unsafe_allow_html=True,
    )
    st.write(
        'Escolhi esse dataset pois acredito que a análise de acidentes de trânsito é uma forma de <span style="color: #FF6161">conscientizar</span> a população sobre a importância da segurança no trânsito e de incentivar ações que visem a redução de acidentes e mortes nas rodovias brasileiras. Além disso, a análise desses dados pode contribuir para a elaboração de <span style="color: #FF6161">políticas públicas</span> e ações de fiscalização que visem a redução de acidentes e mortes no trânsito.',
        unsafe_allow_html=True,
    )

    st.write('## Apresentando o dataset')

    st.write(
        'Depois de selecionarmos as colunas que serão utilizadas na análise, o dataset ficou assim:'
    )
    
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
    st.write(
        'Nele já podemos ver algumas informações sobre os acidentes, como a <span style="color: #FF6161">data</span>, o <span style="color: #FF6161">dia da semana</span>, o <span style="color: #FF6161">município</span>, a <span style="color: #FF6161">causa do acidente</span>, o <span style="color: #FF6161">tipo de acidente</span>, o <span style="color: #FF6161">tipo de veículo</span>, a <span style="color: #FF6161">quantidade de feridos e mortos</span>, entre outros.',
        unsafe_allow_html=True,
    )
    st.divider()
    st.write('## Dicionário de variáveis')
    st.write('A seguir, temos a descrição de cada variável do dataset:')
    col1, col2 = st.columns(2)

    with col1:
        st.write(
            """
        - <span style="color: #FF6161">data_inversa</span>: Data do acidente
        - <span style="color: #FF6161">dia_semana</span>: Dia da semana do acidente
        - <span style="color: #FF6161">uf</span>: Estado onde ocorreu o acidente
        - <span style="color: #FF6161">br</span>: Rodovia onde ocorreu o acidente
        - <span style="color: #FF6161">municipio</span>: Município onde ocorreu o acidente
        - <span style="color: #FF6161">causa_acidente</span>: Causa do acidente
        - <span style="color: #FF6161">tipo_acidente</span>: Tipo do acidente
        - <span style="color: #FF6161">classificacao_acidente</span>: Classificação do acidente
        - <span style="color: #FF6161">fase_dia</span>: Fase do dia do acidente
        - <span style="color: #FF6161">condicao_metereologica</span>: Condição meteorológica no momento do acidente
        - <span style="color: #FF6161">tipo_pista</span>: Tipo da pista
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.write(
            """
        - <span style="color: #FF6161">pessoas</span>: Quantidade de pessoas envolvidas no acidente
        - <span style="color: #FF6161">mortos</span>: Quantidade de mortos no acidente
        - <span style="color: #FF6161">feridos_leves</span>: Quantidade de feridos leves no acidente
        - <span style="color: #FF6161">feridos_graves</span>: Quantidade de feridos graves no acidente
        - <span style="color: #FF6161">ilesos</span>: Quantidade de ilesos no acidente
        - <span style="color: #FF6161">ignorados</span>: Quantidade de pessoas com estado de saúde ignorado
        - <span style="color: #FF6161">feridos</span>: Quantidade total de feridos no acidente
        - <span style="color: #FF6161">veiculos</span>: Quantidade de veículos envolvidos no acidente
        - <span style="color: #FF6161">latitude</span>: Latitude do local do acidente
        - <span style="color: #FF6161">longitude</span>: Longitude do local do acidente
        """,
            unsafe_allow_html=True,
        )
    st.divider()

    st.write('## Hora da Exploração')
    st.write("Antes de começar a explorar os dados, vamos dar uma olhadela nas colunas disponíveis no dataset.")

    col1, col2 = st.columns(2)
    buffer = io.StringIO()
    data.info(buf=buffer)
    s = buffer.getvalue()

    with col1:
        st.code(s)

    st.write('É possível observar que nossas colunas estão sendo tratadas como <span style="color: #FF6161">object</span> e alguns registros estão com o valor <span style="color: #FF6161">None</span>. O que não é o ideal para a análise de dados. Vamos corrigir isso!', unsafe_allow_html=True)

    st.write('### Limpeza e tratamento')
    st.write('Vamos começar tratando os valores ausentes no dataset. Para isso, vamos preencher os valores ausentes com a string <span style="color: #FF6161">Não informado</span>.', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        data.fillna('Não informado', inplace=True)
        st.code('data.fillna("Não informado", inplace=True)', language='python')

    col5, col6 = st.columns([2, 1])
    with col5:
        data['data_inversa'] = pd.to_datetime(data['data_inversa'])
                
        data['dia_semana'] = data['dia_semana'].astype('category')
                
        data['uf'] = data['uf'].astype('category')
                
        data['br'] = data['br'].astype('category')
                
        data['municipio'] = data['municipio'].astype('category')
                
        data['causa_acidente'] = data['causa_acidente'].astype('category')
                
        data['tipo_acidente'] = data['tipo_acidente'].astype('category')
                
        data['classificacao_acidente'] = data['classificacao_acidente'].astype('category')
                
        data['fase_dia'] = data['fase_dia'].astype('category')
                
        data['condicao_metereologica'] = data['condicao_metereologica'].astype('category')
                
        data['tipo_pista'] = data['tipo_pista'].astype('category')
                
        data['latitude'] = data['latitude'].astype('float')
                
        data['longitude'] = data['longitude'].astype('float')

        st.write('Agora, vamos converter as colunas para os tipos de dados corretos.')
        st.code('''
        ### Convertendo o tipo do campo de data
        data['data_inversa'] = pd.to_datetime(data['data_inversa'])
                
        ### Convertendo o tipo das colunas para category
        data['dia_semana'] = data['dia_semana'].astype('category')
                
        data['uf'] = data['uf'].astype('category')
                
        data['br'] = data['br'].astype('category')
                
        data['municipio'] = data['municipio'].astype('category')
                
        data['causa_acidente'] = data['causa_acidente'].astype('category')
                
        data['tipo_acidente'] = data['tipo_acidente'].astype('category')
                
        data['classificacao_acidente'] = data['classificacao_acidente'].astype('category')
                
        data['fase_dia'] = data['fase_dia'].astype('category')
                
        data['condicao_metereologica'] = data['condicao_metereologica'].astype('category')
                
        data['tipo_pista'] = data['tipo_pista'].astype('category')
                
        data['latitude'] = data['latitude'].astype('float')
                
        data['longitude'] = data['longitude'].astype('float')
        ''', language='python')

        new_buffer = io.StringIO()
        data.info(buf=new_buffer)
        ns = new_buffer.getvalue()

        st.write('Agora, vamos verificar se os tipos de dados foram convertidos corretamente.')
        st.code(ns)
    st.write('Pronto! Agora temos os tipos de dados corretos para cada coluna do dataset.')
    st.write('Esse é o resultado final do dataset após a limpeza e tratamento dos dados:')
    st.dataframe(data.head(10))
    