## Repository of Heart Disease predictions service

This service was created as Midterm Project of ml-zoomcamp course

### Context

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worldwide. Four out of 5CVD deaths are due to heart attacks and strokes, and one-third of these deaths occur prematurely in people under 70 years of age. Heart failure is a common event caused by CVDs and this dataset contains 11 features that can be used to predict a possible heart disease.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

### Attribute Information

![image](https://user-images.githubusercontent.com/53815806/139814327-4455227a-cbf1-47cb-8016-a187d947c729.png)
![image](https://user-images.githubusercontent.com/53815806/139814411-29238c49-93b6-4346-b2ee-86bb3bbb791f.png)


### Source
https://ieee-dataport.org/open-access/heart-disease-dataset-comprehensive


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
