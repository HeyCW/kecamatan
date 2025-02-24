import streamlit as st
import pandas as pd
import plotly.express as px
import random


locations = {
    "Lakarsantri": {"lat": -7.3226676, "lon": 112.6116808, "region": "Surabaya Barat"},
    "Dukuhpakis": {"lat": -7.2986816, "lon": 112.638291, "region": "Surabaya Selatan"},
    "Sambikerep": {"lat": -7.2842464, "lon": 112.6248318, "region": "Surabaya Barat"},
    "Wiyung": {"lat": -7.3465284, "lon": 112.6462049, "region": "Surabaya Selatan"},
    "Mulyorejo": {"lat": -7.294421, "lon": 112.7432122, "region": "Surabaya Timur"},
    "Sukomanunggal": {"lat": -7.2713701, "lon": 112.6705405, "region": "Surabaya Barat"},
    "Rungkut": {"lat": -7.3176444, "lon": 112.7585601, "region": "Surabaya Timur"},
    "Pakal": {"lat": -7.2370346, "lon": 112.5891015, "region": "Surabaya Barat"},
    "Sukolilo": {"lat": -7.3059269, "lon": 112.7917378, "region": "Surabaya Timur"},
    "Wonocolo": {"lat": -7.3464022, "lon": 112.7253312, "region": "Surabaya Selatan"},
    "Gubeng": {"lat": -7.2883597, "lon": 112.7419624, "region": "Surabaya Timur"},
    "Waru": {"lat": -7.3464207, "lon": 112.6983369, "region": "Sidoarjo"},
    "Sawahan": {"lat": -7.2801991, "lon": 112.6839514, "region": "Surabaya Selatan"},
    "Tandes": {"lat": -7.2481399, "lon": 112.6300263, "region": "Surabaya Barat"},
    "Tenggilis Mejoyo": {"lat": -7.3397192, "lon": 112.7155956, "region": "Surabaya Timur"},
    "Tegalsari": {"lat": -7.291486, "lon": 112.7112103, "region": "Surabaya Pusat"},
    "Pabean Cantikan": {"lat": -7.2198947, "lon": 112.7100724, "region": "Surabaya Utara"},
    "Wonokromo": {"lat": -7.2930218, "lon": 112.7192555, "region": "Surabaya Selatan"},
    "Trawas": {"lat": -7.6548198, "lon": 112.5437707, "region": "Mojokerto"},
    "Tambaksari": {"lat": -7.2522581, "lon": 112.749022, "region": "Surabaya Timur"},
    "Asem Rowo": {"lat": -7.2241052, "lon": 112.618187, "region": "Surabaya Barat"},
    "Benowo": {"lat": -7.2366432, "lon": 112.5680878, "region": "Surabaya Barat"},
    "Gn. Anyar": {"lat": -7.3382472, "lon": 112.7681798, "region": "Surabaya Timur"},
    "Genteng": {"lat": -7.2570639, "lon": 112.724701, "region": "Surabaya Pusat"},
    "Kenjeran": {"lat": -7.2290555, "lon": 112.7582264, "region": "Surabaya Utara"},
    "Gedangan": {"lat": -7.3886126, "lon": 112.687061, "region": "Sidoarjo"},
    "Krembangan": {"lat": -7.2641236, "lon": 112.6791777, "region": "Surabaya Utara"},
    "Bubutan": {"lat": -7.2520772, "lon": 112.6992812, "region": "Surabaya Pusat"},
    "Buduran": {"lat": -7.426788012, "lon": 112.7578188, "region": "Sidoarjo"},
    "Deket": {"lat": -7.096617612, "lon": 112.4491544, "region": "Lamongan"},
    "Krembung": {"lat": -7.51093014, "lon": 112.6346724, "region": "Sidoarjo"},
    "Gempol": {"lat": -7.5879883, "lon": 112.6804067, "region": "Pasuruan"},
    "Simokerto": {"lat": -7.238716928, "lon": 112.7522951, "region": "Surabaya Pusat"},
    "Penjaringan": {"lat": -7.318660568, "lon": 112.7853252, "region": "Jakarta"},
    "Panggungrejo": {"lat": -7.634956786, "lon": 112.914605, "region": "Pasuruan"},
    "Menganti": {"lat": -7.270427056, "lon": 112.5819241, "region": "Gresik"},
    "Jambangan": {"lat": -7.319057907, "lon": 112.7158848, "region": "Surabaya Selatan"},
    "Pilangkenceng": {"lat": -7.470159092, "lon": 111.6605858, "region": "Madiun"},
    "Kebomas": {"lat": -7.178745049, "lon": 112.6237465, "region": "Gresik"},
    "Berbek": {"lat": -7.342656986, "lon": 112.7597572, "region": "Nganjuk"},
    "Blimbing": {"lat": -7.9468064, "lon": 112.649964, "region": "Malang"},
    "Tuban": {"lat": -6.894457981, "lon": 112.0422661, "region": "Tuban"},
    "Bojonegoro": {"lat": -7.1557159, "lon": 111.8814377, "region": "Bojonegoro"},
    "Tanggulangin": {"lat": -7.507792136, "lon": 112.7195274, "region": "Sidoarjo"},
    "Semampir": {"lat": -7.209501499, "lon": 112.7480509, "region": "Surabaya Utara"},
    "Candi": {"lat": -7.483239619, "lon": 112.7237734, "region": "Sidoarjo"},
    "Taman": {"lat": -7.362494509, "lon": 112.6768603, "region": "Sidoarjo"},
    "Gedeg": {"lat": -7.441533762, "lon": 112.4000748, "region": "Mojokerto"},
    "Nganjuk": {"lat": -7.562138183, "lon": 111.9444172, "region": "Nganjuk"}
}


def get_coordinates(location_name):
    if location_name in locations:
        lat = locations[location_name]['lat']
        lon = locations[location_name]['lon']

        lat += random.uniform(-0.005, 0.005)  
        lon += random.uniform(-0.005, 0.005) 
        
        return lat, lon
    return None, None 

df_location = pd.DataFrame(locations).T.reset_index()

st.title("Visualisasikan berdasarkan Kecamatan")

df = pd.read_excel('Kecamatan.xlsx', engine="openpyxl")

df = df.dropna(subset=['Kecamatan', 'Status Terakhir', 'Tanggal'])

df['Status Terakhir'] = df['Status Terakhir'].str.upper().str.strip()

df[['latitude', 'longitude']] = df['Kecamatan'].apply(lambda x: pd.Series(get_coordinates(x)))

df['region'] = df['Kecamatan'].apply(lambda x: locations[x]['region'])

status = df['Status Terakhir'].unique()

select_status = st.sidebar.multiselect("Pilih Status Terakhir", status)

select_region = st.sidebar.multiselect("Pilih Region", df['region'].unique())

if select_status:
    filtered_df = df[df['Status Terakhir'].isin(select_status)]
else:
    filtered_df = df

if select_region:
    filtered_df = filtered_df[filtered_df['region'].isin(select_region)]
else:
    filtered_df = filtered_df


filtered_df['Tanggal'] = pd.to_datetime(filtered_df['Tanggal'], dayfirst=True, errors='coerce')

filtered_df['Tanggal'] = filtered_df['Tanggal'].dt.date

df_sorted = filtered_df.sort_values(by='Tanggal')

st.write("Data dari file Excel:")
st.dataframe(df_sorted, use_container_width=True)

grouped_region = df_sorted.groupby('region').size().reset_index(name='Jumlah Entri')
grouped_sorted_region = grouped_region.sort_values(by='Jumlah Entri', ascending=False).reset_index(drop=True)


grouped = df_sorted.groupby('Kecamatan').size().reset_index(name='Jumlah Entri')
grouped_sorted = grouped.sort_values(by='Jumlah Entri', ascending=False).reset_index(drop=True)
st.write("Data yang dikelompokkan berdasarkan Kecamatan:")
st.dataframe(grouped_sorted, use_container_width=True)


grouped_time = df_sorted.groupby('Tanggal').size().reset_index(name='Jumlah Entri')
grouped_time = grouped_time.sort_values(by='Tanggal')

st.write("Line Chart: Pengelompokan Data Berdasarkan Waktu (Tanggal)")
st.line_chart(grouped_time.set_index('Tanggal')['Jumlah Entri'], use_container_width=True)


fig1 = px.treemap(grouped_region, 
                    path=['region'], 
                    values='Jumlah Entri', 
                    title='Treemap: Jumlah Entri per Region',
                    color='Jumlah Entri')
                    

st.plotly_chart(fig1)

fig2 = px.treemap(grouped, 
                    path=['Kecamatan'], 
                    values='Jumlah Entri', 
                    title='Treemap: Jumlah Entri per Kecamatan')

st.plotly_chart(fig2)

st.write("Map: Lokasi Kecamatan")
st.map(df_sorted[['latitude', 'longitude']].dropna(how='any'))