import streamlit as st
import pandas as pd
import plotly.express as px

st.write(" # Avocado Prices dashboard")

st.markdown('''
테스트용 데시보드를 만들어 봅시다.    
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')

st.header('Summary statistics')

avocado = pd.read_csv('avocado.csv')
avocado_stats = avocado.groupby('type').mean()
st.dataframe(avocado_stats)

st.header('Line chart by geographies')
line_fig = px.line(avocado[avocado['geography'] == 'Los Angeles'],
                   x='date', y='average_price',
                   color='type',
                   title='Avocado Prices in Los Angeles')
st.plotly_chart(line_fig)



selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
submitted = st.button('Submit')
if submitted:
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)