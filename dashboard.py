# -------------------------
# Bibliotecas importadas
# -------------------------
import geopandas
import folium
import numpy           as np
import pandas          as pd
import streamlit       as st
import plotly_express  as px

from streamlit_folium import folium_static

# -------------------------
# Configurações
# -------------------------
st.set_page_config(layout='wide', initial_sidebar_state='auto')
# Título
st.markdown("<h1 style='text-align: center;'>Northwest Real Estate Agency</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Bem vindo à Northwest Real Estate Agency Data Analysis!</h4>", unsafe_allow_html=True)
st.markdown('Esse projeto de negócio foi elaborado à partir de um banco de dados real. \
             Este banco de dados, público, foi  disponibilizado pelo website Kaggle, um dos maiores websites de competições de Data Science.')
st.markdown('A empresa fictícia Northwest Real Estate Agency tem como objetivo realizar a compra e venda de imóveis na cidade de Seattle (EUA). \
             Com esse objetivo realizei uma análise exploratória, precisa, de todas as informações contidas no banco de dados. \
             Com a conclusão desta análise foi possível aferir as melhores opções de compra de imóveis e, também, a posterior venda dos mesmos, \
             alcançando assim uma margem de lucro real para o time de negócios.')

# -------------------------
# Funções
# -------------------------
# Comando para ler o arquivo diretamente na memória cache
@st.cache(allow_output_mutation=True)
# Carregamento dos dados
def get_data(data):
    data = pd.read_csv(path)
    return data

# Geofile
def get_geofile( url ):
    geofile = geopandas.read_file( url )
    return geofile

# Estatística Descritiva
def statistcs(data):

    df = data.copy()
    num_attributes = df.select_dtypes(include=['int64', 'float64'])
    mini = pd.DataFrame(num_attributes.apply(np.min))
    maxi = pd.DataFrame(num_attributes.apply(np.max))
    media = pd.DataFrame(num_attributes.apply(np.mean))
    mediana = pd.DataFrame(num_attributes.apply(np.median))
    std = pd.DataFrame(num_attributes.apply(np.std))
    desc1 = pd.concat([mini, maxi, media, mediana, std], axis=1).reset_index()
    desc1.columns = ['Atributos', 'Máximo', 'Mínimo', 'Média', 'Mediana', 'Desvio Padrão']

    st.subheader('Estatística Descritiva de Todos os Imóveis do Banco de Dados')
    st.dataframe(desc1)

    return data

# -----------------------------------------------------
# Recomendações de Compra e Aferimento de atributos
# -----------------------------------------------------
def buy_recomm(data, geofile):

        st.header('Selecione os atributos para filtrar as indicações de compra')
        df1 = data.copy()
        median_price = df1[['zipcode', 'price']].groupby('zipcode').median().reset_index()
        df2 = pd.merge(median_price, df1, on='zipcode', how='inner')
        df2 = df2.rename(columns={'price_y': 'price', 'price_x': 'median_price'})

        for x in range(len(df2)):
            if ((df2.loc[x, 'price'] < df2.loc[x, 'median_price']) & (df2.loc[x, 'condition'] >= 3)
                    & (df2.loc[x, 'bedrooms'] >= 1) & (df2.loc[x, 'bathrooms'] >= 1)
                    & (df2.loc[x, 'grade'] >= 7)):
                df2.loc[x, 'purchase'] = 'recommended'

            else:
                df2.loc[x, 'purchase'] = 'rejected'

        buy_list = df2.loc[df2['purchase'] == 'recommended']
        buy_list_prior = buy_list.loc[buy_list['waterfront'] == 'yes']
        df2 = buy_list
        df3 = df2.copy()
        df3['date'] = pd.to_datetime(df3['date'], format=('%Y-%m-%d'))
        df3.loc[df3['bedrooms'] == 33, 'bedrooms'] = 3

        # Barra lateral de seleção e filtros
        st.sidebar.title('Filtro dos Atributos dos Imóveis')
        st.sidebar.markdown('* Selecione os filtros para obter as melhores opções de compra')
        # Filtragem dos Dados pelas Características do Imóveis
        f_bedrooms = st.sidebar.selectbox('Número máx. Quartos',
                                          sorted(df3['bedrooms'].unique()), index=1)
        f_bathrooms = st.sidebar.selectbox('Número máx. Banheiros',
                                           sorted(df3['bathrooms'].unique()), index=4)

        f_zipcode = st.sidebar.multiselect('Códigos Postais - Zipcode', df3['zipcode'].sort_values().unique())
        if f_zipcode != []:
            df3 = df3.loc[df3['zipcode'].isin(f_zipcode), :]
        else:
            df3 = df3.copy()

        c1, c2 = st.columns(2)
        # Sepação pela quantidade de quartos e criação do Histograma
        c1.subheader('Quantidade de Quartos')
        df3 = df3[df3['bedrooms'] < f_bedrooms]
        fig = px.histogram(df3, x='bedrooms', nbins=10, color="bedrooms")
        c1.plotly_chart(fig, use_container_width=True)

        # Sepação pela quantidade de banheiros e criação do Histograma
        c2.subheader('Quantidade de Banheiros')
        df3 = df3[df3['bathrooms'] < f_bathrooms]
        fig = px.histogram(df3, x='bathrooms', nbins=10, color="bathrooms")
        c2.plotly_chart(fig, use_container_width=True)

        # Sepação pela Visão para Água e criação do Histograma
        f_waterview = st.sidebar.checkbox('Imóveis com Vista p/ Água')
        if f_waterview:
            df3 = df3[df3['waterfront'] == 1]
        else:
            df3 = df3.copy()

        min_price = int(data['price'].min())
        max_price = int(data['price'].max())
        avg_price = int(data['price'].mean())
        f_price = st.sidebar.slider('Preço', min_price, max_price, avg_price)
        data = df3.loc[df3['price'] < f_price]

        st.subheader('Imóveis sugeridos para a compra')
        st.markdown('Aqui os imóveis estão agrupados por região ( zipcode ) e dentro de cada região, foi calculada a mediana dos preços por área construída. \
                     Os filtos para a sugestão de compra dos imóveis são os seguintes:  preço abaixo da mediana da região, boas condições \
                     de conservação maior ou igual a 3 (na escala de 1 a 5), tenham um ou mais banheiros e quartos e, também, devem ter uma grade \
                     de classificação maior ou igual a 7 (na escala de 1 a 13).')

        df4 = data.sort_values('price', ascending= True)[['zipcode', 'id', 'price', 'bedrooms', 'bathrooms', 'condition', 'grade',
                                                          'purchase', 'waterfront', 'lat', 'long', 'median_price']]
        df5 = df4[['zipcode', 'id', 'bathrooms', 'bedrooms', 'purchase', 'waterfront', 'condition', 'grade', 'median_price', 'price' ]]
        df5['waterfront'] = df5['waterfront'].apply(lambda x: 'Yes' if x == 1 else 'No')
        st.dataframe(df5)

        # Mapa_1 -> densidade de valores por região
        df_map = df4[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        df_map.columns = ['ZIP', 'PRICE']

        geofile = geofile[geofile['ZIP'].isin(df_map['ZIP'].tolist())]

        map_1 = folium.Map(location=[df4['lat'].mean(),
                                                df4['long'].mean()],
                                      default_zoom_start=15)

        map_1.choropleth(data=df_map,
                                geo_data=geofile,
                                columns=['ZIP', 'PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlGn',
                                fill_opacity=0.7,
                                line_opacity=0.2,
                                legend_name='AVG PRICE')

        st.subheader('Mapa da densidade de preço por região')
        folium_static(map_1)

        # Mapa_2 -> localização real do imóveis
        df_map = df4.copy()
        map_2 = px.scatter_mapbox(df_map, lat='lat', lon='long',
                                 color='price', zoom=10,
                                  color_continuous_scale=px.colors.sequential.Bluered)

        map_2.update_layout(mapbox_style='open-street-map')
        map_2.update_traces(marker={'size': 10})
        map_2.update_layout(height=600, width=800, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

        st.subheader('Mapa da localização real dos imóveis')
        st.plotly_chart(map_2)



        return None

# -------------------------
# Recomendações de Venda
# -------------------------
def sell_recomm(data):

        st.subheader('Uma vez que o imóvel foi comprado, qual é o melhor valor para vendê-lo e qual é a melhor época para concretizar a venda?')
        st.markdown('Os imóveis estão agrupados por região ( zipcode ) e por estação do ano. Dentro de cada região e estação, irei calcular \
                    a mediana do preço. Em seguida calcularemos o percentual de lucro base sobre os imóveis comprados que será de 15 a \
                    35% do valor pago. Assim poderemos ter uma clara noção do preço de venda e também do lucro obtido.')

        data['date'] = pd.to_datetime(data['date'], format=('%Y-%m-%d'))
        data.loc[data['bedrooms'] == 33, 'bedrooms'] = 3
        data['month'] = data['date'].dt.month
        data['year'] = data['date'].dt.year
        data['season'] = data['month'].apply(lambda x: 'summer' if (x > 5) & (x < 8)
                                                    else 'spring' if (x > 2) & (x < 5)
                                                    else 'autumn' if (x > 8) & (x < 12)
                                                    else 'winter')
        df1 = data.copy()
        median_price = df1[['zipcode', 'price']].groupby('zipcode').median().reset_index()
        df2 = pd.merge(median_price, df1, on='zipcode', how='inner')
        df2 = df2.rename(columns={'price_y': 'price', 'price_x': 'median_price'})

        for x in range(len(df2)):
            if ((df2.loc[x, 'price'] < df2.loc[x, 'median_price']) & (df2.loc[x, 'condition'] >= 3)
                    & (df2.loc[x, 'bedrooms'] >= 1) & (df2.loc[x, 'bathrooms'] >= 1)
                    & (df2.loc[x, 'grade'] >= 7)):
                df2.loc[x, 'purchase'] = 'recommended'

            else:
                df2.loc[x, 'purchase'] = 'rejected'

        buy_list = df2.loc[df2['purchase'] == 'recommended']
        buy_list_prior = buy_list.loc[buy_list['waterfront'] == 'yes']
        df2 = buy_list
        df3 = df2.copy()
        df3 = df2[df2['purchase'] == 'recommended']
        df4 = df3[['season', 'zipcode', 'price']].groupby(['zipcode', 'season']).median().reset_index()
        df5 = df4.rename(columns={'price': 'price_med_season', 'season': 'season_med'})
        df6 = pd.merge(df4, df5, on='zipcode', how='inner')

        for x, row in df6.iterrows():
            if (row['price_med_season'] > row['price']):
                df6.loc[x, 'sale'] = row['price'] * 1.15

            else:
                df6.loc[x, 'sale'] = row['price'] * 1.35

        c1, c2 = st.columns(2)
        fig = px.histogram(df6, x='season', y='price', color='season')
        c1.plotly_chart(fig, use_container_width=True)

        df6['profit'] = df6['sale'] - df6['price']
        df6['profit'].sum()
        df7 = df6[['zipcode', 'price', 'sale', 'profit']].groupby('zipcode').mean().reset_index()
        c2.dataframe(df7)

        st.subheader('Concluindo, a projeção máxima de lucros obtidos será de até $52.597.123,00. Isso, claro, levando em consideração os melhores \
         cenários de compra e venda, acima expostos.')

        return data

# -------------------------
# Núcleo do código
# -------------------------
if __name__ == '__main__':
    path = 'csv_files/kc_house_data.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

    # Carregamento
    data = get_data(path)
    geofile = get_geofile( url )


    # Transformação
    statistcs(data)
    buy_recomm(data, geofile)
    sell_recomm(data)
