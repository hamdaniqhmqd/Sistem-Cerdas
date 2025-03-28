# Data penyakit dan gejala
dataPenyakit = {
    "R01": "Penyakit jantung koroner",
    "R02": "Penyakit otot jantung (kardiomiopati)",
    "R03": "Penyakit jantung iskemik",
    "R04": "Penyakit Gagal jantung",
    "R05": "Penyakit jantung hipertensi",
    "R06": "Penyakit katup jantung",
    "R07": "Penyakit Kardiomegali atau jantung hipertrofi"
}

data_gejala = {
    "P001": "Nyeri dada",
    "P002": "Bahu kiri terasa tidak enak",
    "P003": "Keringat dingin",
    "P004": "Sesak nafas",
    "P005": "Gangguan pencernaan",
    "P006": "Mual",
    "P007": "Detak jantung tidak teratur",
    "P008": "Pusing",
    "P009": "Kaki bengkak",
    "P010": "Jantung berdebar-debar",
    "P011": "Mudah lelah",
    "P012": "Nyeri di daerah dada tengah",
    "P013": "Mudah berkeringat",
    "P014": "Dada mengencang",
    "P015": "Pembengkakan pada jantung",
    "P016": "Kelainan fungsi jantung",
    "P017": "Pendarahan dari hidung",
    "P018": "Wajah kemerahan",
    "P019": "Batuk",
    "P020": "Sakit perut",
    "P021": "Detak jantung cepat",
    "P022": "Nyeri di daerah lengan kiri",
    "P023": "Punggung terasa tidak enak",
    "P024": "Sakit Kepala"
}

# Input gejala dari pengguna
input_gejala = input("Gejala (pisahkan dengan koma): ").strip().split(',')
input_gejala = [gejala.strip() for gejala in input_gejala]

# Menampilkan gejala yang dimasukkan
print("\nGejala yang Anda masukkan:")
for gejala in input_gejala:
    print(f"- {gejala}")

# Menyesuaikan gejala dan penyakit dalam kode
gejala_penyakit_map = {
    "R01": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P023"],  # Penyakit jantung koroner
    "R02": ["P004", "P009", "P010", "P011", "P007"],  # Penyakit otot jantung (kardiomiopati)
    "R03": ["P012", "P013", "P014", "P022", "P023"],  # Penyakit jantung iskemik
    "R04": ["P004", "P015", "P016"],  # Gagal jantung
    "R05": ["P024", "P008", "P018", "P011"],  # Penyakit jantung hipertensi
    "R06": ["P011", "P010", "P001", "P004", "P019", "P009"],  # Penyakit katup jantung
    "R07": ["P020", "P007", "P021", "P001"]  # Kardiomegali atau jantung hipertrofi
}

# Proses pencocokan gejala dengan penyakit
gejala_teridentifikasi = False
for penyakit_code, gejala_codes in gejala_penyakit_map.items():
    # Cek apakah semua gejala yang dimasukkan ada dalam gejala penyakit
    if all(data_gejala[code].lower() in [gejala.lower() for gejala in input_gejala] for code in gejala_codes):
        print(dataPenyakit[penyakit_code])
        gejala_teridentifikasi = True
        break

if not gejala_teridentifikasi:
    print("Penyakit tidak teridentifikasi berdasarkan gejala yang diberikan.")

