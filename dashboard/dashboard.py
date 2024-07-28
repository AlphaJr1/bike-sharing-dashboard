import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

st.title('Dashboard Data Penyewaan Sepeda')

season = st.selectbox('Pilih Musim', [1, 2, 3, 4])
filtered_data = day_data[day_data['season'] == season]

st.write('Penyewaan Sepeda pada Musim yang Dipilih')
st.line_chart(filtered_data[['dteday', 'cnt']].set_index('dteday'))

st.write('Penyewaan Sepeda vs Suhu')
st.scatter_chart(filtered_data[['temp', 'cnt']])

st.write('Pengaruh Cuaca terhadap Penyewaan Sepeda')

plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='weathersit', y='cnt')
plt.title('Pengaruh Cuaca terhadap Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')

st.pyplot(plt)
