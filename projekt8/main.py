import numpy as np
import pandas as pd
import ssl
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

headers = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=headers)
print(df.head())

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2023)

# gausian naive bayes classification

nb = GaussianNB()
nb.fit(X_train, y_train)

# walidacja krzyżowa

kfold = KFold(n_splits=5, random_state=2023, shuffle=True)

scores = cross_val_score(nb, X_train, y_train, cv=kfold, scoring="accuracy")

print("Wyniki sprawdzianu krzyżowego:")
print(scores)
print(f"Średnia dokładność: {scores.mean()}")

# ulepszanie

param_grid_nb = {
    'var_smoothing': np.logspace(0, -9, num=100)  # Calculation Stability to Widen (or Smooth) the Curve
}

grid_search = GridSearchCV(nb, param_grid_nb, cv=KFold(n_splits=5, random_state=2023, shuffle=True))
grid_search.fit(X_train, y_train)

results = pd.DataFrame(grid_search.cv_results_)
print(results)
results.to_csv("results.csv")

# wybieranie najlepszego parametru
print("Najlepsze parametry: ", grid_search.best_params_)
print("Najlepszy wynik: ", grid_search.best_score_)

best_model = grid_search.best_estimator_

# sprawdzanie dokładności na zbiorze testowym/treningowym
best_predict = best_model.predict(X_test)
print("Dokładność modelu na zbiorze testowym: ", accuracy_score(y_test, best_predict))

best_predict_train = best_model.predict(X_train)
print("Dokładność na zbiorze treningowym: ", accuracy_score(y_train, best_predict_train))

# macierz pomyłek
cm_train = confusion_matrix(y_train, best_predict_train)
print("Macierz pomyłek dla zbioru treningowego:")
print(cm_train)
report = classification_report(y_train, best_predict_train)
print(report)
