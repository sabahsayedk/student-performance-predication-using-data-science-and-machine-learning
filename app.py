# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 02:53:33 2023

@author: user
"""

# -*- coding: utf-8 -*-


import streamlit as st
import pickle
import streamlit as st

# Load the model from the file
with open('ca3.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a function to make predictions
# giving a title
st.title('student prediction Web App')
st.image("ddd.jpeg")


def predict(input_data):
    # Reshape the input data into a 2D array
    input_data = [float(i) for i in input_data]
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    print(prediction)
    if prediction[0] == 0:
        return 'You have the chance of getting backlog, so study well'
    else:
        return 'You dont have the chance for getting supply,but study well for your academic performance'


def main():
    # Create input fields
    # input_1 = st.text_input('SSLC ')
    input_1 = st.selectbox('SSLC',
                           ['Select', '95%-100%', '90%-95%', '85%-90%', '80%-85%', '75%-80%', '70%-75%', '65%-70%',
                            '60%-65%', '55%-60%', '50%-55%'])
    if input_1 == '95%-100%':
        input_1 = 9
    elif input_1 == '90%-95%':
        input_1 = 8
    elif input_1 == '85%-90%':
        input_1 = 7
    elif input_1 == '80%-85%':
        input_1 = 6
    elif input_1 == '75%-80%':
        input_1 = 5
    elif input_1 == '70%-75%':
        input_1 = 4
    elif input_1 == '65%-70%':
        input_1 = 3
    elif input_1 == '60%-65%':
        input_1 = 2
    elif input_1 == '55%-60%':
        input_1 = 1
    elif input_1 == '50%-55%':
        input_1 = 0

    # input_2 = st.text_input('PLUS TWO')
    input_2 = st.selectbox('PLUS TWO',
                           ['Select', '95%-100%', '90%-95%', '85%-90%', '80%-85%', '75%-80%', '70%-75%', '65%-70%',
                            '60%-65%', '55%-60%', '50%-55%'])
    if input_2 == '95%-100%':
        input_2 = 9
    elif input_2 == '90%-95%':
        input_2 = 8
    elif input_2 == '85%-90%':
        input_2 = 7
    elif input_2 == '80%-85%':
        input_2 = 6
    elif input_2 == '75%-80%':
        input_2 = 5
    elif input_2 == '70%-75%':
        input_2 = 4
    elif input_2 == '65%-70%':
        input_2 = 3
    elif input_2 == '60%-65%':
        input_2 = 2
    elif input_2 == '55%-60%':
        input_2 = 1
    elif input_2 == '50%-55%':
        input_2 = 0

    # input_3 = st.text_input('SLEEP HOUR')
    input_3 = st.selectbox('SLEEP HOUR',
                           ['Select', '0-2 hours', '<=3hours', '<=4hours', '<=5hours', '<=6hours', '<=7hours', '>7hour'])
    if input_3 == '0-2hours':
        input_3 = 0
    elif input_3 == '<=3hours':
        input_3 = 1
    elif input_3 == '<=4hours':
        input_3 = 2
    elif input_3 == '<=5hours':
        input_3 = 3
    elif input_3 == '<=6hours':
        input_3 = 4
    elif input_3 == '<=7hours':
        input_3 = 5
    elif input_3 == '>7hours':
        input_3 = 6

    # input_4 = st.text_input('STUDY HOUR')
    # study time (numeric: 0 - <15 minute,1 - <= 30minute, 2 - <=1hour, 3 - <= 1.5hour,4 - <=2hour,5 - <=2.5hour,6 - >=3hour)
    input_4 = st.selectbox('STUDY HOUR',
                           ['Select', '0-15 minutes', '<=30minutes', '<=1hours', '<=1.5hours', '<=2hours', '<=2.5hours',
                            '>=3hour'])
    if input_4 == '0-15 minutes':
        input_4 = 0
    elif input_4 == '<=30minutes':
        input_4 = 1
    elif input_4 == '<=1hours':
        input_4 = 2
    elif input_4 == '<=1.5hours':
        input_4 = 3
    elif input_4 == '<=2hours':
        input_4 = 4
    elif input_4 == '<=2.5hours':
        input_4 = 5
    elif input_4 == '>=3hours':
        input_3 = 5

    # input_5 = st.text_input('INTEREST OF BTECH STUDIES')
    input_5 = st.selectbox('INTEREST OF BTECH STUDIES', ['Select', 'Yes', 'No'])
    if input_5 == 'Yes':
        input_5 = 1
    else:
        input_5 = 0

    #input_6 = st.text_input('Assignment submission')
    #: Assigment submisson status numeric:1"after the deadline",2"deadline",3"before the deadline")
    input_6 = st.selectbox('Assignment submission',
                            ['Select', 'after the deadline', 'deadline', 'before the deadline'])
    if input_6 == 'after the deadline':
        input_6 = 1
    elif input_6 == 'deadline':
        input_6 = 2
    elif input_6 == 'before the deadline':
        input_6 = 3
    # input_7 = st.text_input('Exam fear')
    input_7 = st.selectbox('Exam fear', ['Select', 'Yes', 'No'])
    if input_7 == 'Yes':
        input_7 = 1
    else:
        input_7 = 0

    # input_8 = st.text_input('PCM Mark')
    input_8 = st.selectbox('PCM Mark',
                           ['Select', '95%-100%', '90%-95%', '85%-90%', '80%-85%', '75%-80%', '70%-75%', '65%-70%',
                            '60%-65%', '55%-60%', '50%-55%'])
    if input_8 == '95%-100%':
        input_8 = 9
    elif input_8 == '90%-95%':
        input_8 = 8
    elif input_8 == '85%-90%':
        input_8 = 7
    elif input_8 == '80%-85%':
        input_8 = 6
    elif input_8 == '75%-80%':
        input_8 = 5
    elif input_8 == '70%-75%':
        input_8 = 4
    elif input_8 == '65%-70%':
        input_8 = 3
    elif input_8 == '60%-65%':
        input_8 = 2
    elif input_8 == '55%-60%':
        input_8 = 1
    elif input_8 == '50%-55%':
        input_8 = 0
    #input_9 = st.text_input('insta reels')
    #instareelsspends :reels spending time (numeric: 0 - <30 min., 1 - 30 to 1 hour., 2 - 1hour. to 1.30 hour, 3 -1.30 to 2 hour,4-2 hour to 3 hour,5 -3hour>)
    input_9 = st.selectbox('insta reels',
                           ['Select', '0-<=30minute', '30minutes-1hours', '1hours to 1.30hours','1.30hours to 2hours','2hours to 3hours','>3hours'])
    if input_9 == '0-<=30minute':
        input_9 = 0
    elif input_9 == '30minutes-1hours':
        input_9 = 1
    elif input_9 == '1hours to 1.30hours':
        input_9 = 2
    elif input_9 == '1.30hours to 2hours':
        input_9 = 3
    elif input_9 == '2hours to 3hours':
        input_9 = 4
    elif input_9 == '>3hours':
        input_9 = 5


    input_10 = st.selectbox('Gender', ['Select', 'male', 'female'])
    if input_10 == 'male':
        input_10 = 1
    else:
        input_10 = 0

    # input_11 = st.text_input('Relationship')
    input_11 = st.selectbox('Relationship', ['Select', 'single', 'committed'])
    if input_11 == 'single':
        input_11 = 1
    else:
        input_11 = 0
    input_12 = st.selectbox('Self learner', ['Select', 'Yes', 'No'])
    if input_12 == 'Yes':
        input_12 = 1
    else:
        input_12 = 0
    # input_12 = st.text_input('self learner')
    # input_13 = st.text_input('frequent sickness')
    # input_13 = st.selectbox('frequent sickness', ['Select', 'Yes', 'No'])
    # if input_13 == 'Yes'
    #   input_13 = 1
    # else:
    #   input_13 = 0

    # input_13 = st.text_input('frequent sickness')
    input_13 = st.selectbox('frequent sickness', ['Select', 'Yes', 'No'])
    if input_13 == 'Yes':
        input_13 = 1
    else:
        input_13 = 0

    input_14 = st.selectbox('Extracurricularactivity', ['Select', 'Yes', 'No'])
    if input_14 == 'Yes':
        input_14 = 1
    else:
        input_14 = 0

    # input_15 = st.text_input('studypreparation')
    input_15 = st.selectbox('studypreparation',
                            ['Select', 'daily preparation', 'weekly preparation', 'monthly preparation'])
    if input_15 == 'daily preparation':
        input_15 = 1
    elif input_15 == 'weekly preparation':
      input_15 = 2
    elif input_15 == 'monthly preparation':
      input_15 = 3



    input_16 = st.selectbox('programming', ['Select', 'Yes', 'No'])
    if input_16 == 'Yes':
        input_16 = 1
    else:
        input_16 = 0

    # Create a button to trigger the prediction
    if st.button('Predict'):
        result = predict(
            [input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9, input_10, input_11,
             input_12, input_13, input_14, input_15, input_16])
        st.write('Prediction: ', result)


if __name__ == '__main__':
    main()
