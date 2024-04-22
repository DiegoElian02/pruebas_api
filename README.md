# FastAPI Machine Learning Model

This project is a simple FastAPI application that uses a pre-trained machine learning model to make predictions. The model is a Random Forest classifier that has been trained and serialized using Python's `pickle` module.

## Getting Started

To get started with this project, clone the repository and install the necessary dependencies.

```bash
git clone <https://github.com/DiegoElian02/pruebas_api.git>
cd <repository>
pip install -r requirements.txt
```

## Running the Application
To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on your local machine.

## API Endpoints
The application has a single API endpoint:

* /predict/: This endpoint accepts GET requests with the following parameters: Pclass, Age, SibSp, Parch, Embarked_C, Embarked_Q, Embarked_S, is_male. It returns a JSON response with the prediction from the model.

## Example
Here is an example of how to use the /predict/ endpoint:

```bash
curl -X GET "http://localhost:80/predict/?Pclass=3&Age=22.0&SibSp=1&Parch=0&Embarked_C=0&Embarked_Q=0&Embarked_S=1&is_male=1"
```
This will return a JSON response like the following:

```bash
{
  "prediction": 0
}
```