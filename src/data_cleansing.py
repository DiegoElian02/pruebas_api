import pandas as pd
#import numpy as np
#from sklearn.impute import KNNImputer

# def fill_na_knn(df : pd.DataFrame(), columna : str, neighbors : int):

#     knn_imputer = KNNImputer(n_neighbors = neighbors)
#     idx = list(df.columns).index(columna)
#     c = knn_imputer.fit_transform(df)
#     df[columna] =  c[:,idx]
#     return train

def remove_outliers(df, rango : float, columna :  str):
    # Select only numeric columns
    df_c = df[[columna]]
    numeric_cols = df_c.select_dtypes(include=['number'])

    # Calculate Q1, Q3, and IQR for numeric columns
    Q1 = numeric_cols.quantile(0.25)
    Q3 = numeric_cols.quantile(0.75)
    IQR = Q3 - Q1

    # Apply the filter only to numeric columns
    mask = ~((numeric_cols < (Q1 - rango * IQR)) | (numeric_cols > (Q3 + rango * IQR))).any(axis=1)

    # Create a new DataFrame using the filter condition
    return df[mask]


train = pd.read_csv(r"data\train.csv")
train = train.drop(columns = ['Cabin', 'PassengerId', 'Ticket', 'Name'])

train[train['Fare']== train['Fare'].max()]
train = remove_outliers(train, 13, 'Fare')

train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
train['Age'] = train['Age'].fillna(train['Age'].mean())

train = pd.get_dummies(train, columns=['Embarked'])
train['is_male'] = pd.get_dummies(train['Sex'])['male']
train = train.drop(columns='Sex')

train = train.drop(columns = ['Fare'], axis = 1)

train.to_csv(r"data\train_clean.csv", index = False)