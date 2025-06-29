import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBRegressor

# Завантаження моделі
model = joblib.load("C:/Users/Dorosh/Project/Superstore Dataset/profit_xgb.pkl")

st.title("💰 Прогноз прибутку для замовлення")

# Інтерактивна форма
sales = st.number_input("Sales", min_value=0.0, step=0.25)
discount = st.slider("Discount", min_value=0.0, max_value=0.90, step=0.05)
quantity = st.number_input("Quantity", min_value=1, step=1)

category = st.selectbox("Category", ["Furniture", "Office Supplies", "Technology"])
sub_category = st.selectbox("Sub-Category", ['Bookcases', 'Chairs', 'Labels', 'Tables', 'Storage',
                                             'Furnishings', 'Art', 'Phones', 'Binders', 'Appliances', 'Paper',
                                             'Accessories', 'Envelopes', 'Fasteners', 'Supplies', 'Machines','Copiers'])

segment = st.selectbox("Segment", ["Consumer", "Corporate", "Home Office"])
region = st.selectbox("Region", ["West", "East", "Central", "South"])
ship_mode = st.selectbox("Ship Mode", ['Second Class', 'Standard Class', 'First Class', 'Same Day'])

# Збір у DataFrame
user_input = pd.DataFrame([{
    "Sales": sales,
    "Discount": discount,
    "Quantity": quantity,
    "Category": category,
    "Sub-Category": sub_category, 
    "Segment": segment,
    "Region": region,
    "Ship Mode": ship_mode
}])

# Кнопка прогнозу
if st.button("🔮 Передбачити прибуток"):
    prediction = model.predict(user_input)[0]
    st.success(f"Прогнозований прибуток: {prediction:.2f} $")

    if prediction < 0:
        st.warning("⚠️ Це замовлення потенційно збиткове!")
    elif prediction < 15:
        st.info("ℹ️ Малий прибуток. Можливо варто зменшити знижку.")
    else:
        st.balloons()
        st.success("✅ Це вигідне замовлення!")
