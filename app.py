import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

st.title("Spam Message Classifier")

message = st.text_area("Enter your message")

if st.button("Check Message"):

    data = vectorizer.transform([message])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Spam Message")
    else:
        st.success("Not Spam")