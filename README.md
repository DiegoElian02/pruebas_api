# FastAPI Machine Learning Model

This project is a simple FastAPI application that uses a pre-trained machine learning model to make predictions. The model is a Random Forest classifier that has been trained and serialized using Python's `pickle` module.

## Getting Started

To get started with this project, clone the repository, build the container and run it

```bash
git clone https://github.com/DiegoElian02/pruebas_api.git
cd pruebas_api
docker build -t titanic_api .
```

## Running the Application
To run the container that runs the app, use the following command:

```bash
docker run -p 80:80 titanic_api
```

This will start the Docker container and the FastAPI server on your local machine.

## API Endpoints
The application has a single API endpoint:

* /predict/: This endpoint accepts GET requests with the following parameters: Pclass, Age, SibSp, Parch, Embarked_C, Embarked_Q, Embarked_S, is_male. It returns a JSON response with the prediction from the model.

## Example
Here is an example of how to use the /predict/ endpoint:

```bash
curl "http://localhost:80/predict/?Pclass=3&Age=22.0&SibSp=1&Parch=0&Embarked_C=0&Embarked_Q=0&Embarked_S=1&is_male=1"
```
This will return a JSON response like the following:

```bash
{
  "prediction": 0
}
```