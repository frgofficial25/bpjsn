import pandas as pd
import math

path_input = 'D:/UB/FRG/bpjsn/2025/Data Sampel Reguler Edisi 2025/data/202402_fktpkapitasi.csv.gz'
path_out1 = 'D:/UB/FRG/bpjsn/2025/Data Sampel Reguler Edisi 2025/data/202402_fktpkapitasi_part1.csv.gz'
path_out2 = 'D:/UB/FRG/bpjsn/2025/Data Sampel Reguler Edisi 2025/data/202402_fktpkapitasi_part2.csv.gz'

print("1. Sedang membaca seluruh file asli (mohon tunggu)...")
# low_memory=False dan dtype=str untuk mencegah warning tipe data campuran
df = pd.read_csv(path_input, low_memory=False, dtype=str)

# Hitung total baris dan bagi dua
total_baris = len(df)
titik_tengah = math.ceil(total_baris / 2)
print(f"Total data: {total_baris} baris. Akan dibagi menjadi masing-masing {titik_tengah} baris.")

print("2. Memotong dan menyimpan Part 1...")
df_part1 = df.iloc[:titik_tengah]
df_part1.to_csv(path_out1, compression='gzip', index=False)

print("3. Memotong dan menyimpan Part 2...")
df_part2 = df.iloc[titik_tengah:]
df_part2.to_csv(path_out2, compression='gzip', index=False)

print("Selesai! Part 1 dan Part 2 berhasil dibuat dengan jumlah baris seimbang.")
