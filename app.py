from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
import math
import numpy as np
import tensorflow as tf
import pickle
import uuid

app = Flask(__name__)
app.secret_key = "Emotion_Detection_Messenger"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
  session['user_id'] = 0
  if request.method == 'POST':
    session['user_id'] = uuid.uuid4()
    session['message_list'] = []
    session['emotion_1'] = ""
    session['emotion_2'] = ""
    return redirect("/message")
  else:
    return render_template('index.html')


@app.route('/reset', methods=['GET', 'POST'])
def reset():
  if request.method == 'POST':
    session['message_list'] = []
    session['emotion_1'] = ""
    session['emotion_2'] = ""
  
  return redirect('/message')

@app.route('/go_back', methods=['GET', 'POST'])
def go_back():
  if request.method == 'POST':
    return redirect('/')

@app.route('/message', methods=['GET', 'POST'])
def message():
  if(session['user_id'] == 0):
    return redirect('/')
  else:
    all_message = session['message_list']
    if request.method == 'POST': 
      message = request.form['message']
      sender = request.form['sender']
      timestamp = math.trunc(time.time())

      message_dict = {
        "sender" : int(sender),
        "message" : message
      }

      all_message.append(message_dict)
      session['message_list'] = all_message
      return redirect("/message")
    else:
      if(len(all_message) !=  0):
        message_to_evaluate = all_message[len(all_message) - 1]
        emotion = emotion_detection([message_to_evaluate.get('message')])
        send = int(message_to_evaluate.get('sender'))
        if send == 1:
          session['emotion_1'] = emotion
        else:
          session['emotion_2'] = emotion

      all_messages = session['message_list']
      return render_template('message.html', all_messages = all_messages, emotion_1 = session['emotion_1'], emotion_2 = session['emotion_2'])



# Emotion detection
def emotion_detection(sentence):
  classNames = np.load("./static/model/class_names.npy")

  with open('./static/model/tokenizer.pickle', 'rb') as handle:
    Tokenizer = pickle.load(handle)
  
  model = tf.keras.models.load_model("./static/model/model_final.model")
  MAX_LENGTH = maxen = 100

  sentence_processed = Tokenizer.texts_to_sequences(sentence)
  sentence_processed = np.array(sentence_processed)
  sentence_padded = tf.keras.preprocessing.sequence.pad_sequences(sentence_processed, padding='post', maxlen=MAX_LENGTH)

  result = model.predict(sentence_padded)
  return classNames[np.argmax(result)]
  
