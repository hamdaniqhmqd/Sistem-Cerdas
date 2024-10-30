def Validasi_Data (ipk, penghasilan_ortu, sanksi) :
  if (ipk >= 3.0 and penghasilan_ortu <= 2000000 and not sanksi) :
    return "Mahasiswa berhak mendapatkan beasiswa"
  else : 
    return "Mahasiswa tidak berhak mendapatkan beasiswa"

ipk = float(input("Masukkan nilai IPK mahasiswa : "))
penghasilan_ortu = float(input("Masukkan penghasilan orang tua Mahasiswa : "))
sanksi = str(input("Apakah mahasiswa pernah mendapatkan sanksi (y/n) : ")).lower()

if (sanksi == 'y') :
  sanksi_mhs = True
else :
  sanksi_mhs = False

hasil = Validasi_Data(ipk, penghasilan_ortu, sanksi_mhs)
print(hasil)