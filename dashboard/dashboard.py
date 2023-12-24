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
 

with st.sidebar:

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



st.header('Ifandi Bike Sharing :sparkles:')



# Membuat dataframe dari data harian untuk rentang waktu yang dipilih
selected_data_range['dteday'] = pd.to_datetime(selected_data_range['dteday'])
day_df_range = create_day_df(selected_data_range)

# Membuat dataframe dari data musim
data_season = {
    'season': [1, 2, 3, 4],
    'cnt_mean': [2604.132597, 4992.331522, 5644.303191, 4728.162921],
    'cnt_std': [1399.942119, 1695.977235, 1459.800381, 1699.615261]
}
df_season = pd.DataFrame(data_season)

# Plotting diagram garis untuk musim
fig_season, ax_season = plt.subplots(figsize=(10, 6))
ax_season.plot(df_season['season'], df_season['cnt_mean'], marker='o', color='blue', label='Rata-rata Sewa Sepeda')
ax_season.errorbar(df_season['season'], df_season['cnt_mean'], yerr=df_season['cnt_std'], fmt='o', color='blue', capsize=5, label='Error Bar (Std)')
ax_season.set_xlabel('Musim')
ax_season.set_ylabel('Jumlah Rata-rata Sewa Sepeda')
ax_season.set_title('Perbandingan Jumlah Rata-rata Sewa Sepeda Antara Musim')
ax_season.set_xticks(df_season['season'])
ax_season.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
ax_season.legend()
ax_season.grid(True)

# Membuat dataframe dari data jam
data_hour = {
    'hr': list(range(24)),
    'cnt_mean': [53.898072, 33.375691, 22.869930, 11.727403, 6.352941, 19.889819, 76.044138, 212.064649, 
                 359.011004, 219.309491, 173.668501, 208.143054, 253.315934, 253.661180, 240.949246, 
                 251.233196, 311.983562, 461.452055, 425.510989, 311.523352, 226.030220, 172.314560, 131.335165, 87.831044],
    'cnt_std': [42.307910, 33.538727, 26.578642, 13.239190, 4.143818, 13.200765, 55.084348, 161.441936,
                235.189285, 93.703458, 102.205413, 127.495536, 145.081134, 148.107657, 147.271574, 144.632541,
                148.682618, 232.656611, 224.639304, 161.050359, 119.670164, 89.788893, 69.937782, 50.846889]
}
df_hour = pd.DataFrame(data_hour)

# Plotting diagram garis untuk jam
fig_hour, ax_hour = plt.subplots(figsize=(10, 6))
ax_hour.plot(df_hour['hr'], df_hour['cnt_mean'], marker='o', color='blue', label='Rata-rata Sewa Sepeda')
ax_hour.errorbar(df_hour['hr'], df_hour['cnt_mean'], yerr=df_hour['cnt_std'], fmt='o', color='blue', capsize=5, label='Error Bar (Std)')
ax_hour.set_xlabel('Jam (hr)')
ax_hour.set_ylabel('Jumlah Rata-rata Sewa Sepeda')
ax_hour.set_title('Perbandingan Jumlah Rata-rata Sewa Sepeda Per Jam')
ax_hour.legend()
ax_hour.grid(True)

# Membuat DataFrame untuk RFM
data_rfm = {
    'dteday': ['2011-01-01'],
    'recency': [5],
    'frequency': [3],
    'cnt': [985]
}
rfm_df = pd.DataFrame(data_rfm)

# Plotting diagram batang untuk RFM
fig_rfm, axes_rfm = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
axes_rfm[0].bar(rfm_df['dteday'], rfm_df['recency'], color='#72BCD4')
axes_rfm[0].set_title('Recency')
axes_rfm[1].bar(rfm_df['dteday'], rfm_df['frequency'], color='#72BCD4')
axes_rfm[1].set_title('Frequency')
axes_rfm[2].bar(rfm_df['dteday'], rfm_df['cnt'], color='#72BCD4')
axes_rfm[2].set_title('Monetary (cnt)')

plt.tight_layout()

# Tampilkan gambar-gambar Matplotlib di Streamlit
st.pyplot(fig_season)
st.pyplot(fig_hour)
st.pyplot(fig_rfm)
