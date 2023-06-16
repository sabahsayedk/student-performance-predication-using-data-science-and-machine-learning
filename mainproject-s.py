# -*- coding: utf-8
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load your trained model
s_model = pickle.load(open('C:/Users/user/Desktop/main project finalize/ss', 'rb'))

# Define the main function
def main():
  with st.sidebar:
    # Create the dropdown menu
    selected = option_menu('student performance predication')
                          
    if (selected== 'student performace predication'):
      st.title('student performance predication using ml')
      
   
      
     
