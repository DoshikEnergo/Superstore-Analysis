# 💰 Superstore Profit Predictor

A simple and intuitive web app that predicts **profit** for a customer order in a Superstore, based on key order parameters such as **sales**, **discount**, **category**, and more.

Built with **Streamlit** and powered by a trained **XGBoost regression model**.

---

## 📸 Preview

![App Screenshot](./917a1ae6-b16d-491f-8f44-acd93acf99e4.png)

---

## 🚀 Features

- Interactive web interface (no coding required!)
- Predicts profit based on:
  - Sales amount
  - Discount level
  - Quantity
  - Product category and sub-category
  - Customer segment
  - Region and shipping mode
- Visual feedback: success, warning, or risk of loss
- Real-time response using a pre-trained machine learning model

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – web interface
- **XGBoost** – regression model
- **Pandas** – data handling
- **Joblib** – loading the trained model

---

## ⚙️ How to Run

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/superstore-profit-predictor.git
cd superstore-profit-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas xgboost joblib
```

### 3. Make sure you have the trained model

Place your model file `profit_xgb.pkl` in the correct path.

If your file is in a different location, update this line in `app.py`:
```python
model = joblib.load("C:/Users/Dorosh/Project/Superstore Dataset/profit_xgb.pkl")
```

### 4. Launch the app

```bash
streamlit run "path/to/app.py"
```

For example:
```bash
streamlit run "C:/Users/Dorosh/Project/Superstore Dataset/app.py"
```

---

## 📂 File Structure

```
├── app.py                  # Main application
├── profit_xgb.pkl          # Trained XGBoost model
├── requirements.txt        # List of dependencies
├── 917a1ae6...png          # Screenshot (optional)
└── *.ipynb                 # Notebook (optional, for training/debugging)
```

---

## 🧾 Input Fields

| Field         | Description                       |
|---------------|-----------------------------------|
| Sales         | Order amount                      |
| Discount      | Discount on the order (0–90%)     |
| Quantity      | Number of units                   |
| Category      | Main product category             |
| Sub-Category  | Specific product sub-type         |
| Segment       | Type of customer (e.g. Corporate) |
| Region        | Delivery region                   |
| Ship Mode     | Type of delivery                  |

---

## ✅ Output

- 🎯 **Predicted Profit** (in USD)
- 🟢 *Success alert* if profit is good
- 🟡 *Info* if profit is low
- 🔴 *Warning* if order is likely unprofitable

---

## 👤 Author

**Dmytro Doroshenko**  
Student | Data Science Enthusiast | Energy Specialist