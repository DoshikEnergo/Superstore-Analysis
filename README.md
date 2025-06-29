# Superstore-Analysis
💰 Superstore Profit Predictor
This is a Streamlit web application that predicts the profit of an order based on various features such as sales, discount, category, and more. It uses a trained XGBoost regression model.

🧠 Technologies Used
Python

Streamlit – for building the interactive web interface

XGBoost – machine learning model (regression)

Joblib – to load the saved model

Pandas – for data handling

🚀 How to Run the App
Clone the repository or download the project:

bash
Copy
Edit
git clone https://github.com/yourusername/superstore-profit-predictor.git
cd superstore-profit-predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, here’s a minimal one:

text
Copy
Edit
streamlit
pandas
xgboost
joblib
Launch the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open the app in your browser and enter the order details to get the profit prediction.

📁 Project Structure
pgsql
Copy
Edit
├── app.py                         # Streamlit application
├── profit_xgb.pkl                 # Trained XGBoost model (must be present!)
└── Superstore Dataset-checkpoint.ipynb   # (Optional) Jupyter notebook for analysis/preparation
🧾 Input Features
Sales – Order amount

Discount – Discount rate (0–90%)

Quantity – Quantity of items

Category – Product category

Sub-Category – Product sub-category

Segment – Customer segment

Region – Delivery region

Ship Mode – Delivery method

✅ Prediction Results
If the predicted profit is negative → ⚠️ This order may result in a loss!

If the profit is below $15 → ℹ️ Low profit. You may want to reduce the discount.

If the profit is above $15 → 🎉 Profitable order!

⚠️ Note
Make sure the model file is available at the correct path:

python
Copy
Edit
model = joblib.load("C:/Users/Dorosh/Project/Superstore Dataset/profit_xgb.pkl")
Otherwise, update the path according to your local setup.

👤 Author
Dmytro Doroshenko

This project was created as part of learning Python, Data Science, and Streamlit.

