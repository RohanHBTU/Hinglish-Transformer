import streamlit as st
import pickle
import pandas as pd
import numpy
import tensorflow as tf
import tensorflow_text as tf_text
from metaphone import doublemetaphone
import re

with open('vocab_data.pkl', 'rb') as fp:
    hin_vocab = pickle.load(fp)
vocab_keys=[l for l in hin_vocab]
#all_data_vocab_53k_mixed_batch_v2
reloaded = tf.saved_model.load("translator")

def t_text(line):
    line=re.sub("[.!?\\-\'\"]", "",line).lower().strip()
    string=''
    for j in line.split(' '):
        if doublemetaphone(j)[0]+'*'+doublemetaphone(j[::-1])[0]+'*'+j[:2]+'*'+j[len(j)-1:] in vocab_keys:
            string=string+list(hin_vocab[doublemetaphone(j)[0]+'*'+doublemetaphone(j[::-1])[0]+'*'+j[:2]+'*'+j[len(j)-1:]])[0]+' '
        else:
            string=string+j+' '
    return string.lower().strip()


st.header("Hinglish-English Translator")

st.subheader("Please enter your text!")
st.text("")

input = st.text_area("Enter here")

if st.button('Check Now!'):
    #transformed_sms = transform_text(input)
    #vector_input = tfidf.transform([transformed_sms])
    #result = model.predict(vector_input)[0]
    #if result == 1:
    #    st.error("Spam")
    #else:
    #    st.success("Not Spam")
    st.write(reloaded.tf_translate(
            tf.constant([
                t_text(input)
                        ]))['text'][0].numpy().decode())
    #st.write(t_text(input))
    #st.write("Thank you! I hope you liked it. ")
    #st.write("Check out this Repo's [GitHub Link](https://github.com/RohanHBTU/spam_classifier)")
