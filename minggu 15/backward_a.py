class PenyakitKulit:

    def __init__(self, nama, gejala, solusi):
        self.nama = nama
        self.gejala = gejala
        self.solusi = solusi
        
aturan = [
    {"condition": ["pembengkakan kulit", "benjolan di kulit"], "consequence": "Jerawat"},
    {"condition": ["bernanh", "demam"], "consequence": "Bisul"},
    {"condition": ["mata merah", "kulit kepala berminyak"], "consequence": "Campak"},
    {"condition": ["merasa gatal", "luka dibagian mulut"], "consequence": "Ketombe"},
    {"condition": ["bergelembar isi air", "nyeri"], "consequence": "Hypohidrosis"},
]

def backward_chaining(tujuan, aturan, penyakit_kulit, gejala_user):
    for penyakit in penyakit_kulit:
        if penyakit.nama == tujuan:
            if all(gejala.lower() in gejala_user for gejala in penyakit.gejala):
                return penyakit.nama, penyakit.solusi

    return "Tidak ditemukan penyakit yang cocok", []
  
def main():
    """
    Fungsi utama program.
    """
    print("Selamat datang di Sistem Pakar Penyakit Kulit!")
    gejala_user = []
    while True:
        gejala = input("Masukkan gejala yang Anda alami (ketik 'selesai' untuk berhenti): ")
        if gejala.lower() == 'selesai':
            break
        gejala_user.append(gejala.lower())

    diagnosis, solusi = backward_chaining(tujuan, aturan, gejala_user)
    print(f"Diagnosis: {diagnosis}")
            
if __name__ == "__main__":
    main()