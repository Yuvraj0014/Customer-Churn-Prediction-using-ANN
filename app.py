import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
import pickle

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Load the encoders and scaler
with open('onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
st.set_page_config(page_title='Customer Churn Prediction', layout='wide')
st.title('🤖 Customer Churn Prediction')
st.markdown('---')

# User input
st.markdown('## 📋 Enter Customer Details')

col1, col2 = st.columns(2)

with col1:
    geography = st.selectbox('🌍 Geography', onehot_encoder_geo.categories_[0])
    age = st.slider('👨‍🦳 Age', 18, 92, value=18)
    credit_score = st.number_input('🏦 Credit Score', min_value=0, max_value=850, value=0)
    num_of_products = st.slider('🛒 Number of Products', 1, 4, value=1)
    is_active_member = st.selectbox('🧑‍💻 Is Active Member', [0, 1], index=0)

with col2:
    gender = st.selectbox('👨‍🦱👩‍🦱 Gender', label_encoder_gender.classes_)
    balance = st.number_input('💰 Balance', min_value=0.0, value=0.0)
    estimated_salary = st.number_input('💸 Estimated Salary', min_value=0.0, value=0.0)
    tenure = st.slider('📆 Tenure', 0, 10, value=0)
    has_cr_card = st.selectbox('💳 Has Credit Card', [0, 1], index=0)

# Prepare the input data as a DataFrame
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Concatenate One-hot encoded column with input data
input_data = pd.concat([input_data, geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)

# Predict churn
prediction = model.predict(input_data_scaled)
prediction_prob = prediction[0][0]

# Display prediction and result
col1, col2, col3 = st.columns(3)
with col1:
    pass
with col2:
    st.markdown('## 🔮 Predict Churn')
    if st.button('Predict'):
        st.markdown('## 🧠 Churn Prediction')
        st.write(f'Churn Probability: {prediction_prob:.2f} 📊')

        if prediction_prob > 0.5:
            st.write('The customer is likely to churn. 😥')
        else:
            st.write('The customer is unlikely to churn. 😊')
with col3:
    pass