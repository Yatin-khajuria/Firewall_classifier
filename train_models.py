import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import joblib

df = pd.read_csv("http_requests_dataset.csv")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["request"])
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestClassifier()
knn = KNeighborsClassifier()
svm = SVC()

rf.fit(X_train, y_train)
knn.fit(X_train, y_train)
svm.fit(X_train, y_train)

joblib.dump(vectorizer, "vectorizer.joblib")
joblib.dump(rf, "rf_model.joblib")
joblib.dump(knn, "knn_model.joblib")
joblib.dump(svm, "svm_model.joblib")
