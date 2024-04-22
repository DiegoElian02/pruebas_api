import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import random
import pickle
random.seed(0)

def titanic_rf_tuned(n_trees, dep: int, X_train, y_train, X_test, y_test, maxfeatures):

    classifier = RandomForestClassifier(n_estimators=n_trees,
                                        max_depth= dep,
                                        random_state=0,
                                        min_samples_leaf=5,
                                        max_features= maxfeatures
                                        )
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    acc = accuracy_score(y_test,prediction)

    # Create a Confusion Matrix
    matrix = pd.DataFrame(
            confusion_matrix(y_test, prediction),
            columns=['Predicted 0', 'Predicted 1'],
            index=['Actual 0', 'Actual 1'])
    return acc, matrix, classifier

train = pd.read_csv(r"data\train_clean.csv")
y = train.Survived  
X  = train.drop(columns = "Survived")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, shuffle=False)

accuracy, c_matrix, model = titanic_rf_tuned(150,9, X_train, y_train, X_test, y_test, "sqrt")

with open(r"models\model.pkl", "wb") as f:
    pickle.dump(model, f)
