# 🏦 Customer Churn Prediction App 🤖

## 📋 Project Overview
This is a sophisticated customer churn prediction web application built with Streamlit and TensorFlow. The app predicts whether a bank customer is likely to leave the bank's services based on various customer attributes. 

🧠 The prediction model is powered by Artificial Neural Networks (ANN), meticulously trained on historical customer data to identify complex patterns associated with customer churn. The deep learning model processes customer information through multiple neural layers to provide:
- ⚡ Real-time predictions
- 📊 Probability scores
- 🎯 High accuracy predictions
- 🔄 Consistent results

Making it an effective tool for proactive customer retention strategies in the banking sector.

## 💻 Requirements
```python
# Core Dependencies
numpy         # For numerical operations
pandas        # For data manipulation
streamlit     # For web interface
tensorflow    # For neural network model
scikit-learn  # For data preprocessing
pickle        # For model serialization
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

## 🎯 Prediction Output
Once all data is entered, click the '🔮 Predict' button to receive:

### 1. Churn Probability Score 📊
   - Range: 0.00 - 1.00
   - Higher score = Higher churn risk
   
### 2. Prediction Interpretation 📈
   - High Risk (> 0.5): "⚠️ The customer is likely to churn" 😥
   - Low Risk (≤ 0.5): "✅ The customer is unlikely to churn" 😊

## 🚀 How to Run
```bash
# Launch the application
streamlit run app.py
```

---
*Built with ❤️ for better customer retention*
