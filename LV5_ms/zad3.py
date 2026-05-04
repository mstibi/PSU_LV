import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, precision_score, recall_score

import matplotlib.pyplot as plt


# 1. Učitavanje podataka

data = pd.read_csv("occupancy_processed.csv")




X = data[['S3_Temp', 'S5_CO2']]
y = data['Room_Occupancy_Count']

# 2. Podjela 

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Skaliranje 




# 4. Stablo odlučivanja

model = DecisionTreeClassifier(max_depth=5, random_state=42)

model.fit(X_train, y_train)


# 5. Predikcija

y_pred = model.predict(X_test)


# 6. Evaluacija

print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
print("\nTočnost:", accuracy)

preciznost = precision_score(y_test, y_pred)
print("\nPreciznost:", preciznost)

odziv = recall_score(y_test, y_pred)
print("\nOdziv: ", odziv)


# 7. Vizualizacija stabla

plt.figure(figsize=(12, 8))
plot_tree(model,
          feature_names=['temperature', 'co2'],
          class_names=['0', '1'],
          filled=True)
plt.show()