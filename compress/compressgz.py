import os
import pandas as pd

FOLDER_UTAMA = "D:/UB/FRG/bpjsn/2025"

def compress_csv_to_gz(folder_target):
    print("=" * 60)
    print(f"Memulai kompresi super .csv -> .csv.gz di: {folder_target}")
    print("=" * 60)
    
    total_awal = 0
    total_akhir = 0
    counter = 0
    
    for root, dirs, files in os.walk(folder_target):
        for file in files:
            if file.endswith('.csv') and not file.endswith('.csv.gz'):
                file_path = os.path.join(root, file)
                gz_path = file_path + '.gz'
                
                ukuran_awal = os.path.getsize(file_path)
                total_awal += ukuran_awal
                
                try:
                    print(f"[Super Compress] -> {file}")
                    df = pd.read_csv(file_path, low_memory=False)
                    
                    # Simpan langsung ke format gzip
                    df.to_csv(gz_path, index=False, compression='gzip')
                    
                    # Hapus file .csv asli yang boros tempat
                    os.remove(file_path)
                    
                    ukuran_akhir = os.path.getsize(gz_path)
                    total_akhir += ukuran_akhir
                    counter += 1
                except Exception as e:
                    print(f"❌ Gagal mengompres {file}: {e}")
                    total_akhir += ukuran_awal
                    
    if total_awal > 0:
        mb_awal = total_awal / (1024 * 1024)
        mb_akhir = total_akhir / (1024 * 1024)
        print("=" * 60)
        print(f"SELESAI! {counter} file berhasil diciutkan.")
        print(f"Ukuran Awal : {mb_awal:.2f} MB")
        print(f"Ukuran Akhir: {mb_akhir:.2f} MB (Hemat {(1 - mb_akhir/mb_awal)*100:.1f}%) 🔥")
        print("=" * 60)

if __name__ == "__main__":
    if os.path.exists(FOLDER_UTAMA):
        compress_csv_to_gz(FOLDER_UTAMA)
