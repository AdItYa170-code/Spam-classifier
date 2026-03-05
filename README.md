# Spam Message Classifier

This project detects whether a message is **Spam or Not Spam** using Machine Learning.

## Features
- Detects spam messages
- Uses NLP (TF-IDF Vectorization)
- Naive Bayes machine learning model
- Simple Streamlit web interface

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- NLP (TF-IDF)

## How It Works
1. The dataset of SMS messages is loaded.
2. Text is converted into numerical form using TF-IDF.
3. A Naive Bayes model is trained.
4. The model predicts whether a message is spam or not.

## Run the Project

Install libraries:

pip install pandas scikit-learn streamlit

Run the web app:

streamlit run app.py

## Example

Input:
Congratulations! You won a free lottery ticket

Output:
Spam Message

## Author
Aditya Kumar