import joblib
import numpy as np


model = joblib.load('model_iris_v1.joblib')
metadata = joblib.load('metadata_v1.joblib')

print(f"Model: {metadata['model_type']}")
print(f"Wersja: {metadata['model_version']}")
print(f"Dokładność na zbiorze testowym: {metadata['accuracy']:.4f}")
print(f"Cechy: {metadata['features']}")
print(f"Klasy: {metadata['classes']}")

# przykładowy rekord do predykcji (powinno wyjść setosa)
sample = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = model.predict(sample)
prediction_proba = model.predict_proba(sample)

print(f"Dane wejściowe: {sample[0]}")
print(f"Przewidywana klasa: {metadata['classes'][prediction[0]]}")
print(f"Prawdopodobieństwa: {prediction_proba[0]}")
print(f"Dla każdej klasy: {metadata['classes']}")