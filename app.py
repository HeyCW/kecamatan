import streamlit as st
import pandas as pd
import plotly.express as px




st.title("Visualisasikan berdasarkan Kecamatan")

df = pd.read_excel('Kecamatan.xlsx', engine="openpyxl")

df['Status Terakhir'] = df['Status Terakhir'].str.upper().str.strip()

status = df['Status Terakhir'].unique()

select_status = st.sidebar.multiselect("Pilih Status Terakhir", status)

if select_status:
    filtered_df = df[df['Status Terakhir'].isin(select_status)]
else:
    filtered_df = df

filtered_df['Tanggal'] = pd.to_datetime(filtered_df['Tanggal'], dayfirst=True, errors='coerce')

filtered_df['Tanggal'] = filtered_df['Tanggal'].dt.date

df_sorted = filtered_df.sort_values(by='Tanggal')

st.write("Data dari file Excel:")
st.dataframe(df_sorted, use_container_width=True)

grouped = df_sorted.groupby('Kecamatan').size().reset_index(name='Jumlah Entri')
grouped_sorted = grouped.sort_values(by='Jumlah Entri', ascending=False).reset_index(drop=True)
st.write("Data yang dikelompokkan berdasarkan Kecamatan:")
st.dataframe(grouped_sorted, use_container_width=True)


grouped_time = df_sorted.groupby('Tanggal').size().reset_index(name='Jumlah Entri')
grouped_time = grouped_time.sort_values(by='Tanggal')

# Menampilkan Line Chart
st.write("Line Chart: Pengelompokan Data Berdasarkan Waktu (Tanggal)")
st.line_chart(grouped_time.set_index('Tanggal')['Jumlah Entri'], use_container_width=True)

fig = px.treemap(grouped, 
                    path=['Kecamatan'], 
                    values='Jumlah Entri', 
                    title='Treemap: Jumlah Entri per Kecamatan')

st.plotly_chart(fig)