import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, recall_score

# 1. Učitavanje podataka

data = pd.read_csv("occupancy_processed.csv")

X = data[['S3_Temp', 'S5_CO2']]
y = data['Room_Occupancy_Count']


# 2. Podjela skupa

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Skaliranje podataka

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# 4. KNN klasifikator

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train_scaled, y_train)

# 5. Predikcija

y_pred = knn.predict(X_test_scaled)

# 6. Evaluacija

# Matrica zabune
cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(cm)

# Metrike
accuracy = accuracy_score(y_test, y_pred)
print("\nTočnost:", accuracy)

rezultati = classification_report(y_test, y_pred)
print("\Rezultati:", rezultati)
