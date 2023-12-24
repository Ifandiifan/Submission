import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Dapatkan path absolut dari direktori skrip saat ini
script_directory = os.path.dirname(os.path.abspath(__file__))

# Gabungkan dengan nama file untuk membentuk path lengkap
file_path = os.path.join(script_directory, 'all_data.csv')

print(file_path)
all_df = pd.read_csv(file_path)

def create_day_df(df):
    # Menghitung jumlah penyewaan harian
    day_df = df.groupby('dteday')['cnt'].sum().reset_index()
    # Mengganti nama kolom
    day_df.rename(columns={'cnt': 'total_rentals'}, inplace=True)
    return day_df

def create_hour_df(df):
    # Menghitung jumlah penyewaan harian
    hour_df = df.groupby('dteday')['cnt'].sum().reset_index()
    # Mengganti nama kolom
    hour_df.rename(columns={'cnt': 'total_rentals'}, inplace=True)
    return hour_df

# ... (sisa fungsi-fungsi dan data frame tetap sama)

# Pastikan min_date dan max_date adalah objek datetime.date
min_date = pd.to_datetime(all_df["dteday"].min()).date()
max_date = pd.to_datetime(all_df["dteday"].max()).date()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/Ifandiifan/Logo/main/bike%20sharing.jpg")
    
   # ...

with st.sidebar:
    # ...

    # Pilih rentang waktu yang ingin ditampilkan
    selected_start_date = st.date_input(
        label='Pilih Tanggal Awal',
        min_value=min_date,
        max_value=max_date,
        value=min_date  # Tanggal default
    )

    selected_end_date = st.date_input(
        label='Pilih Tanggal Akhir',
        min_value=min_date,
        max_value=max_date,
        value=max_date  # Tanggal default
    )

    # Filter data sesuai dengan rentang waktu yang dipilih
    selected_data_range = all_df[(all_df["dteday"] >= str(selected_start_date)) & (all_df["dteday"] <= str(selected_end_date))]

# ...

st.header('Ifandi Bike Sharing :sparkles:')

# ...

# Tampilkan data
st.write(f"Data untuk rentang waktu {selected_start_date} hingga {selected_end_date}:")
st.write(selected_data_range)

# ...



data = {
    'season': [1, 2, 3, 4],
    'cnt_mean': [2604.132597, 4992.331522, 5644.303191, 4728.162921],
    'cnt_std': [1399.942119, 1695.977235, 1459.800381, 1699.615261]
}

# ...

# Membuat dataframe dari data harian untuk rentang waktu yang dipilih
day_df_range = create_day_df(selected_data_range)

# Plotting diagram garis
plt.figure(figsize=(10, 6))
plt.plot(day_df_range['dteday'], day_df_range['total_rentals'], marker='o', color='green', label='Total Rentals')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Total Sewa Sepeda')
plt.title('Grafik Jumlah Total Sewa Sepeda Harian')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# ...

