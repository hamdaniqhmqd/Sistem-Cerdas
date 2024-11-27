dataPenyakit = {
    "DP1": "Diare",
    "DP2": "Kejang Demam",
    "DP3": "Bronchopneumonia",
    "DP4": "Asma",
    "DP5": "Cacingan"
}

dataGejala = {
    "DG1": "Bab cair lebih dari 3x sehari",
    "DG2": "Lesu",
    "DG3": "Nafsu makan berkurang",
    "DG4": "Keram pada perut",
    "DG5": "Perut kembung",
    "DG6": "Demam",
    "DG7": "Muntah",
    "DG8": "Kejang 1-2x sehari",
    "DG9": "Bab cair",
    "DG10": "Sesak nafas",
    "DG11": "Terlihat sangat mengantuk",
    "DG12": "Batuk",
    "DG13": "Pilek",
    "DG14": "Menggigil",
    "DG15": "Dada terasa sakit",
    "DG16": "Sakit kepala",
    "DG17": "Nafas berbunyi (mengi)",
    "DG18": "Faktor keturunan",
    "DG19": "Susah tidur",
    "DG20": "Anak tampak kurus",
    "DG21": "Pucat",
    "DG22": "Gatal sekitar anus",
    "DG23": "Gelisah atau tidak nyaman saat tidur",
    "DG24": "Iritasi kulit sekitar anus",
    "DG25": "Sering sakit perut"
}

input_gejala = input("Gejala (pisahkan dengan koma): ").strip().split(',')
input_gejala = [gejala.strip() for gejala in input_gejala]

print("\nGejala yang Anda masukkan:")
for gejala in input_gejala:
    print(f"- {gejala}")

print("\nPenyakit yang teridentifikasi:")

if any(dataGejala[gejala_code].lower() == gejala.lower() for gejala_code in ["DG1", "DG2", "DG3", "DG4", "DG5", "DG6", "DG7"] for gejala in input_gejala):
    print(dataPenyakit["DP1"])

elif any(dataGejala[gejala_code].lower() == gejala.lower() for gejala_code in ["DG6", "DG7", "DG9", "DG10", "DG11", "DG12", "DG13"] for gejala in input_gejala):
    print(dataPenyakit["DP2"])

elif any(dataGejala[gejala_code].lower() == gejala.lower() for gejala_code in ["DG3", "DG6", "DG10", "DG12", "DG14", "DG15", "DG16"] for gejala in input_gejala):
    print(dataPenyakit["DP3"])

elif any(dataGejala[gejala_code].lower() == gejala.lower() for gejala_code in ["DG2", "DG10", "DG12", "DG17", "DG18", "DG19"] for gejala in input_gejala):
    print(dataPenyakit["DP4"])

elif any(dataGejala[gejala_code].lower() == gejala.lower() for gejala_code in ["DG20", "DG21", "DG22", "DG23", "DG24", "DG25"] for gejala in input_gejala):
    print(dataPenyakit["DP5"])

else:
    print("Penyakit tidak teridentifikasi berdasarkan gejala yang diberikan.")
