import numpy as np
import pandas as pd
from numpy.testing.print_coercion_tables import print_coercion_table
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
feature_names = iris.feature_names

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y
df['target_names'] = df['target'].apply(lambda x: target_names[x])

print('Informacje o zbierze:')
print(df.shape)
print(df.head(5))
print('-----------------------------------------')
print(df.info())
print('-----------------------------------------')
print(df.describe())
print('-----------------------------------------')

print("Stworzenie prostego modelu ML:")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Rozmiar zbioru treningowego: {len(X_train)} próbek")
print(f"Rozmiar zbioru testowego: {len(X_test)} próbek")

# Utworzenie i wytrenowanie modelu
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Predykcja i ocena modelu
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Dokładność modelu: {accuracy:.4f}")
print("Raport klasyfikacji:")
print(classification_report(y_test, y_pred, target_names=target_names))

joblib.dump(model, 'model_iris_v1.joblib')

# metadane
metadata = {
    'model_version': 'v1.0',
    'model_type': 'LogisticRegression',
    'accuracy': accuracy,
    'features': feature_names,
    'classes': target_names.tolist(),
    'train_size': len(X_train),
    'test_size': len(X_test)
}

joblib.dump(metadata, 'metadata_v1.joblib')

