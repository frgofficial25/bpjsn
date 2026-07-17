import os
import pandas as pd

# Tentukan folder target tempat data BPJS Anda berada
FOLDER_UTAMA = "D:/UB/FRG/bpjsn/2025"

def convert_ke_csv_rekursif(folder_target):
    print("=" * 60)
    print(f"Memulai konversi rekursif ke .csv di: {folder_target}")
    print("=" * 60)
    
    counter_dta = 0
    counter_xlsx = 0
    
    # Menyusur semua subfolder secara rekursif hingga terdalam
    for root, dirs, files in os.walk(folder_target):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 1. KONVERSI FILE .dta KE .csv
            if file.endswith('.dta'):
                try:
                    csv_path = file_path.replace('.dta', '.csv')
                    print(f"[Konversi .dta -> .csv] -> {file}")
                    
                    # Baca data Stata
                    df = pd.read_stata(file_path)
                    # Simpan ke CSV dengan kompresi string standar
                    df.to_csv(csv_path, index=False)
                    
                    # HAPUS file .dta asli setelah sukses konversi
                    os.remove(file_path)
                    counter_dta += 1
                except Exception as e:
                    print(f"❌ Gagal mengonversi .dta {file}: {e}")
            
            # 2. KONVERSI FILE .xlsx KE .csv
            elif file.endswith('.xlsx'):
                try:
                    csv_path = file_path.replace('.xlsx', '.csv')
                    print(f"[Konversi .xlsx -> .csv] -> {file}")
                    
                    # Baca semua sheet di Excel
                    excel_file = pd.read_excel(file_path, sheet_name=None)
                    
                    # Gabungkan sheet jika ada lebih dari satu, atau simpan sheet pertama
                    for sheet_name, df_sheet in excel_file.items():
                        # Jika ada multi-sheet, beri nama file_sheetname.csv
                        if len(excel_file) > 1:
                            csv_path_multi = file_path.replace('.xlsx', f'_{sheet_name}.csv')
                            df_sheet.to_csv(csv_path_multi, index=False)
                        else:
                            df_sheet.to_csv(csv_path, index=False)
                    
                    # HAPUS file .xlsx asli setelah sukses konversi
                    os.remove(file_path)
                    counter_xlsx += 1
                except Exception as e:
                    print(f"❌ Gagal mengonversi .xlsx {file}: {e}")

    print("=" * 60)
    print("PROSES KONVERSI SELESAI!")
    print(f"Berhasil mengubah {counter_dta} file .dta menjadi .csv")
    print(f"Berhasil mengubah {counter_xlsx} file .xlsx menjadi .csv")
    print("=" * 60)

if __name__ == "__main__":
    if os.path.exists(FOLDER_UTAMA):
        convert_ke_csv_rekursif(FOLDER_UTAMA)
    else:
        print("❌ Folder tidak ditemukan.")
