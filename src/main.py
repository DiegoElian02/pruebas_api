from fastapi import FastAPI#, Query
import numpy as np
import pickle

app = FastAPI()

# Cargar el modelo de Random Forest
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.get("/predict/")
async def predict(Pclass: int, Age: float, SibSp: int, Parch: int, 
                  Embarked_C: int, Embarked_Q: int, Embarked_S: int, 
                  is_male: int):
    # Preparar el vector de entrada para el modelo
    input_features = np.array([[Pclass, Age, SibSp, Parch, 
                                Embarked_C, Embarked_Q, Embarked_S, is_male]])
    # Hacer la predicción
    prediction = model.predict(input_features)
    # Devolver la predicción
    return {"prediction": int(prediction[0])}
