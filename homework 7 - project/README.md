## Repository of Heart Disease predictions service

This service was created as Midterm Project of ml-zoomcamp course conducted by Alexey Grigorev (https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp)

### Context

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

### Attribute Information

* Age: age of the patient [years]
* Sex: sex of the patient [M: Male, F: Female]
* ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
* RestingBP: resting blood pressure [mm Hg]
* Cholesterol: serum cholesterol [mm/dl]
* FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
* RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
* MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
* ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
* Oldpeak: oldpeak = ST [Numeric value measured in depression]
* ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
* HeartDisease: output class [1: heart disease, 0: Normal]

### Source
https://www.kaggle.com/fedesoriano/heart-failure-prediction


## Notes
Requirements for the project are described here https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project

### Dependency and enviroment management
Pipenv is used as python virtual environment.
You can install all requirements with command ```pipenv install``` in the project directory.
After installing the required libraries we can run the project in the virtual environment with ```pipenv shell``` command.

### Containerization
To build docker image use command
```
docker build -t heartdisease-prediction .
```
to run it
```
docker run --rm -it -p 9696:9696 heartdisease-prediction:latest
```


### Cloud deployment

This project was deployed to Heroku cloud.
To deploy this project you don't need any additional code, just create file Procfile with 1 line: ```web: gunicorn predict:app``` and follow the official guide to push this repo to Heroku - https://devcenter.heroku.com/articles/git

In predict_test.ipynb Jupyter notebook you can find how to test the service endpoint.
