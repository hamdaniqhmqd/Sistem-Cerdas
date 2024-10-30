kota_list = ["bali", "lombok", "yogyakarta", "malang"]

Aktivitas = ["wisata budaya", "bermain air", "kuliner", "wisata gunung", "wisata anak"]

hubungan = {
    "bali" : ["wisata budaya", "bermain anak", "pedesaan"],
    "lombok" : ["mendaki gunung", "wisata alam", "bermain air"],
    "yogyakarta" : ["wisata budaya", "wisata sejarah", "kuliner"],
    "malang" : ["wisata gunung", "kuliner", "wisata anak"],
}

Aktivitas_tujuan = ["kuliner"]

kota_tujuan_ditemukan = False

for kota in kota_list:
    if set(Aktivitas_tujuan).issubset(hubungan[kota]):
        print(f"Wisata {Aktivitas_tujuan[0]} tersebut ada di kota {kota}")
        kota_tujuan_ditemukan = True

if not kota_tujuan_ditemukan:
    print("Wisata tidak diketahui di kota mana")
