penyakit = ["flu", "demam berdarah", "malaria"]

gejala = ["demam", "batuk", "pilek", "sakit kepala", "nyeri otot"]

hubungan = {
  "flu" : ["demam", "batuk", "pilek"],
  "demam berdarah" : ["demam tinggi", "bintik merah pada kulit"],
  "malaria" : ["demam", "mengigil", "sakit kepala", "nyeri otot"],
}

gejala_pasien = ["demam", "batuk", "pilek"]

for penyakit in penyakit :
  if set(gejala_pasien).issubset(hubungan[penyakit]) :
    print("Pasien menderita", penyakit)
    break

else:
  print("Pasien tidak menderita penyakit flu, demam berdarah, atau malaria")