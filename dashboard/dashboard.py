
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

data = {
    'season': [1, 2, 3, 4],
    'cnt_mean': [2604.132597, 4992.331522, 5644.303191, 4728.162921],
    'cnt_std': [1399.942119, 1695.977235, 1459.800381, 1699.615261]
}
df = pd.DataFrame(data)

all_df = pd.read_csv("all_data.csv")
df = all_df.drop_duplicates()
summary_stats = df.describe()

def extract_year_from_date(date):
    return pd.to_datetime(date).year


df['year'] = df['dteday'].apply(extract_year_from_date)

def group_data_by_hour(df):
    return df.groupby('hr')['cnt'].sum().reset_index()


hourly_grouped_data = group_data_by_hour(df)


def filter_data_by_year(df, year):
    return df[df['year'] == year]


filtered_data_2011 = filter_data_by_year(df, 2011)

# Pastikan min_date dan max_date adalah objek datetime.date
min_date = pd.to_datetime(all_df["dteday"].min()).date()
max_date = pd.to_datetime(all_df["dteday"].max()).date()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/Ifandiifan/Logo/main/bike%20sharing.jpg")
    
   #Pilih tanggal yang ingin ditampilkan
selected_date = st.date_input(
    label='Pilih Tanggal',
    min_value=pd.to_datetime(all_df["dteday"].min()).date(),
    max_value=pd.to_datetime(all_df["dteday"].max()).date(),
    value=pd.to_datetime(all_df["dteday"].min()).date()  # Tanggal default
)

# Filter data sesuai dengan tanggal yang dipilih
selected_data = all_df[all_df["dteday"] == str(selected_date)]

# Tampilkan data
st.write(f"Data untuk tanggal {selected_date}:")
st.write(selected_data)


st.header('Ifandi Bike Sharing :sparkles:')

data = {
    'season': [1, 2, 3, 4],
    'cnt_mean': [2604.132597, 4992.331522, 5644.303191, 4728.162921],
    'cnt_std': [1399.942119, 1695.977235, 1459.800381, 1699.615261]
}

# Membuat dataframe dari data
df = pd.DataFrame(data)

# Plotting diagram garis
plt.figure(figsize=(10, 6))
plt.plot(df['season'], df['cnt_mean'], marker='o', color='blue', label='Rata-rata Sewa Sepeda')
plt.errorbar(df['season'], df['cnt_mean'], yerr=df['cnt_std'], fmt='o', color='blue', capsize=5, label='Error Bar (Std)')
plt.xlabel('Musim')
plt.ylabel('Jumlah Rata-rata Sewa Sepeda')
plt.title('Perbandingan Jumlah Rata-rata Sewa Sepeda Antara Musim')
plt.xticks(df['season'], ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
plt.legend()
plt.grid(True)
plt.show()

data = {
    'hr': list(range(24)),
    'cnt_mean': [53.898072, 33.375691, 22.869930, 11.727403, 6.352941, 19.889819, 76.044138, 212.064649, 
                 359.011004, 219.309491, 173.668501, 208.143054, 253.315934, 253.661180, 240.949246, 
                 251.233196, 311.983562, 461.452055, 425.510989, 311.523352, 226.030220, 172.314560, 131.335165, 87.831044],
    'cnt_std': [42.307910, 33.538727, 26.578642, 13.239190, 4.143818, 13.200765, 55.084348, 161.441936,
                235.189285, 93.703458, 102.205413, 127.495536, 145.081134, 148.107657, 147.271574, 144.632541,
                148.682618, 232.656611, 224.639304, 161.050359, 119.670164, 89.788893, 69.937782, 50.846889]
}

# Membuat dataframe dari data
df = pd.DataFrame(data)

# Plotting diagram garis
plt.figure(figsize=(10, 6))
plt.plot(df['hr'], df['cnt_mean'], marker='o', color='blue', label='Rata-rata Sewa Sepeda')
plt.errorbar(df['hr'], df['cnt_mean'], yerr=df['cnt_std'], fmt='o', color='blue', capsize=5, label='Error Bar (Std)')
plt.xlabel('Jam (hr)')
plt.ylabel('Jumlah Rata-rata Sewa Sepeda')
plt.title('Perbandingan Jumlah Rata-rata Sewa Sepeda Per Jam')
plt.legend()
plt.grid(True)
plt.show()

data = {
    'dteday': ['2011-01-01'],
    'recency': [5],
    'frequency': [3],
    'cnt': [985]
}

# Membuat DataFrame
rfm_df = pd.DataFrame(data)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
axes[0].bar(rfm_df['dteday'], rfm_df['recency'], color='#72BCD4')
axes[0].set_title('Recency')
axes[1].bar(rfm_df['dteday'], rfm_df['frequency'], color='#72BCD4')
axes[1].set_title('Frequency')
axes[2].bar(rfm_df['dteday'], rfm_df['cnt'], color='#72BCD4')
axes[2].set_title('Monetary (cnt)')

plt.tight_layout()
plt.show()
