import os
import pandas as pd

# Tentukan folder target tempat data CSV BPJS Anda berada
FOLDER_UTAMA = "D:/UB/FRG/bpjsn/2025"

def ciutkan_isi_csv_rekursif(folder_target):
    print("=" * 60)
    print(f"Memulai pengecilan ukuran internal teks .csv di: {folder_target}")
    print("=" * 60)
    
    counter = 0
    for root, dirs, files in os.walk(folder_target):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                print(f"[Menghemat Teks CSV] -> {file}")
                
                try:
                    # 1. Baca CSV (low_memory=False agar tidak memakan RAM berlebih)
                    df = pd.read_csv(file_path, low_memory=False)
                    
                    # 2. Trik Utama 1: Cari kolom desimal (float), bulatkan maksimal 2 angka di belakang koma
                    # Ini akan membuang ratusan karakter angka nol atau ekor desimal yang tidak penting
                    kolom_desimal = df.select_dtypes(include=['float64', 'float32']).columns
                    for col in kolom_desimal:
                        df[col] = df[col].round(2)
                    
                    # 3. Trik Utama 2: Bersihkan spasi kosong (whitespace) tersembunyi di kolom teks/string
                    kolom_teks = df.select_dtypes(include=['object']).columns
                    for col in kolom_teks:
                        if df[col].dtype == 'object':
                            df[col] = df[col].astype(str).str.strip()
                    
                    # 4. Simpan kembali ke file CSV yang sama, tanpa index bawaan pandas
                    df.to_csv(file_path, index=False)
                    counter += 1
                    
                except Exception as e:
                    print(f"❌ Gagal memproses {file}: {e}")
                    
    print("=" * 60)
    print(f"SELESAI! {counter} file .csv berhasil dihemat ukuran fisiknya secara permanen!")
    print("=" * 60)

if __name__ == "__main__":
    if os.path.exists(FOLDER_UTAMA):
        ciutkan_isi_csv_rekursif(FOLDER_UTAMA)
    else:
        print("❌ Folder tidak ditemukan.")
