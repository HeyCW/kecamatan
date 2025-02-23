import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Visualisasikan berdasarkan Kecamatan")

df = pd.read_excel('Kecamatan.xlsx', engine="openpyxl")

df['Tanggal'] = pd.to_datetime(df['Tanggal'], dayfirst=True, errors='coerce')

df['Tanggal'] = df['Tanggal'].dt.date

df_sorted = df.sort_values(by='Tanggal')

st.write("Data dari file Excel:")
st.dataframe(df, use_container_width=True)

grouped = df.groupby('Kecamatan').size().reset_index(name='Jumlah Entri')
grouped_sorted = grouped.sort_values(by='Jumlah Entri', ascending=False).reset_index(drop=True)
st.write("Data yang dikelompokkan berdasarkan Kecamatan:")
st.dataframe(grouped_sorted, use_container_width=True)


grouped_time = df.groupby('Tanggal').size().reset_index(name='Jumlah Entri')
grouped_time = grouped_time.sort_values(by='Tanggal')

# Menampilkan Line Chart
st.write("Line Chart: Pengelompokan Data Berdasarkan Waktu (Tanggal)")
st.line_chart(grouped_time.set_index('Tanggal')['Jumlah Entri'], use_container_width=True)

st.write("Treemap: Jumlah Entri per Kecamatan")
fig = px.treemap(grouped, 
                    path=['Kecamatan'],  # Membuat path berdasarkan Kecamatan
                    values='Jumlah Entri',  # Jumlah entri sebagai ukuran
                    title='Treemap: Jumlah Entri per Kecamatan')

# Menampilkan Treemap
st.plotly_chart(fig)

