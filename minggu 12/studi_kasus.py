# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Menggunakan dataset contoh (Misalnya predictive maintenance dataset)
# Gantilah dengan dataset Anda sendiri
df = pd.read_csv('dataCar/CarPrice_Assignment.csv')

# Memeriksa data awal
print(df.head())

# Data Preprocessing
# Menangani missing values (bisa dengan imputation atau drop)
df.fillna(df.mean(), inplace=True)

# Mengonversi variabel kategorikal menjadi numerik jika ada
label_encoder = LabelEncoder()
df['failure'] = label_encoder.fit_transform(df['failure'])

# Pisahkan fitur dan label
X = df.drop(columns=['failure'])
y = df['failure']

# Split data ke dalam train dan test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Membuat model RandomForestClassifier
rf_model = RandomForestClassifier(random_state=42)

# Optimasi hyperparameter dengan GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, scoring='accuracy', verbose=1)
grid_search.fit(X_train, y_train)

# Menampilkan hasil terbaik
print("Best parameters found: ", grid_search.best_params_)

# Menggunakan model terbaik dari GridSearchCV
best_rf_model = grid_search.best_estimator_

# Prediksi pada test set
y_pred = best_rf_model.predict(X_test)

# Evaluasi Model
print(f"Accuracy: {accuracy_score(y_test, y_pred): .4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

