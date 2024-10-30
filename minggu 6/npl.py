import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Contoh teks
text = """
Natural Language Processing (NLP) adalah bidang kecerdasan buatan yang berfokus pada interaksi antara komputer dan manusia menggunakan bahasa alami. 
NLP bertujuan untuk membaca, memahami, dan menghasilkan bahasa manusia dengan cara yang bernilai.
"""

# Tokenisasi
words = word_tokenize(text.lower())  # Mengubah ke huruf kecil untuk konsistensi

# Menghapus stopwords
stop_words = set(stopwords.words('indonesian'))  # Anda dapat menggunakan 'english' untuk bahasa Inggris
filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

# Menghitung frekuensi kata
word_counts = Counter(filtered_words)

# Menampilkan hasil
print("Frekuensi Kata:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
