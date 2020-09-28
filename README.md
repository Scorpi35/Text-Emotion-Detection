# Message Emotion Detection

## Project Details
This project aims to detect emotions from messages. 

## Dataset
* Name:- ISEAR Dataset (https://www.kaggle.com/shrivastava/isears-dataset)
* Instances:- 7516
* Columns:- label, text
* Emotions(label):- Anger, Disgust, Fear, Guilt, Joy, Sadness, Shame 

## Framework
Flask (Python)

## Algoritm
1. Pre-processing Dataset
2. Tokenization
3. Generate word embeddings
4. Training LSTM Model with bidirectional layers

## Model Training Description
* Layers:- 1 Embedding layer, 3 Bidirectional layers, 2 Dense layers
* Optimizer:- Adam
* Epoch:- 150
* Batch Size:- 120
* Validation Split:- 0.2

## Results

## Screenshots

![alt text](https://github.com/Scorpi35/Flask-Emotion-Detection/blob/master/images/Screen%20Shot%202020-09-25%20at%2016.49.58.png)
![alt text](https://github.com/Scorpi35/Flask-Emotion-Detection/blob/master/images/Screen%20Shot%202020-09-25%20at%2017.19.59.png)




