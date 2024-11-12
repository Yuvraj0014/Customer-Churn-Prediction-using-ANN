  # 🏦 Customer Churn Prediction App using Artificial Neural Network 🤖

## 📋 Project Overview
This is a sophisticated customer churn prediction web application built with Streamlit and TensorFlow. The app predicts whether a bank customer is likely to leave the bank's services based on various customer attributes. 

🧠 The prediction model is powered by Artificial Neural Networks (ANN), meticulously trained on historical customer data to identify complex patterns associated with customer churn. The deep learning model processes customer information through multiple neural layers to provide:
- ⚡ Real-time predictions
- 📊 Probability scores
- 🎯 High accuracy predictions
- 🔄 Consistent results

Making it an effective tool for proactive customer retention strategies in the banking sector.

## 💻 Requirements

1. tensorflow
2. pandas
3. numpy
4. scikit-learn
5. tensorboard
6. matplotlib
7. streamlit
8. scikeras

## Installation
To run the project locally, follow these steps:

1. Clone the repository:

```cmd
git clone https://github.com/Yuvraj0014/Customer-Churn-Prediction-using-ANN.git
Customer-Churn-Prediction-using-ANN
```

2. Setup a virtual environment (optional but recommended)
```cmd
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate  # For Windows
```

3. Install required dependencies
```cmd
pip install -r requirements.txt
```

4. Run the streamlit app
```cmd
streamlit run app.py
```

## 🚀 Usage
The application features an intuitive interface divided into two panels for easy data input:

### 📝 Left Panel Features:
1. **Geography** 🌍
   - Select customer's location
   - Supports multiple regions
   
2. **Age** 👨‍🦳
   - Slider input: 18-92 years
   - Easy age selection
   
3. **Credit Score** 💯
   - Range: 0-850
   - Numerical input field
   
4. **Number of Products** 🛍️
   - Range: 1-4 products
   - Slider selection
   
5. **Active Member Status** 👤
   - Binary selection: Yes (1) / No (0)
   - Indicates account activity

### 📝 Right Panel Features:
1. **Gender** 👥
   - Binary gender selection
   - Preprocessed by encoder
   
2. **Balance** 💰
   - Current account balance
   - Accepts decimal values
   
3. **Estimated Salary** 💵
   - Annual salary input
   - Numerical field
   
4. **Tenure** ⏳
   - Years with bank: 0-10
   - Slider selection
   
5. **Credit Card Status** 💳
   - Has card: Yes (1) / No (0)
   - Binary selection

## 🎯 Output Prediction
Once all data is entered, click the '🔮 Predict' button to receive:

### 1. Churn Probability Score 📊
   - Range: 0.00 - 1.00
   - Higher score = Higher churn risk
   
### 2. Prediction Interpretation 📈
   - High Risk (> 0.5): "⚠️ The customer is likely to churn" 😥
   - Low Risk (≤ 0.5): "✅ The customer is unlikely to churn" 😊

## 📸 Application Interface
Below is a screenshot of the application's user interface showing the input parameters and prediction output. The interface is designed to be user-friendly with clear sections for data input and prominent display of the churn prediction results.
![image](https://github.com/user-attachments/assets/80791239-df06-4cc0-bb25-070bd8c69568)

## 🎯 Output Screen
![image](https://github.com/user-attachments/assets/158ab3a2-e980-4d04-bedb-e5d9d1fe1fc0)

## Results 
Too lazy to adult today? Join the club! Ditch the to-do list and dive into the Streamlight app instead. It's right here, waiting for you!
```
customer-churn-prediction-using-ann.streamlit.app
```


