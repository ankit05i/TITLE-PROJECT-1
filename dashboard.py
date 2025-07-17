
import streamlit as st
import joblib

model = joblib.load("traffic_model.pkl")

st.title("🚦 Traffic Congestion Predictor")

st.header("Enter Input Details:")
hour = st.slider("Hour of the Day (0-23):", 0, 23, 12)
day_of_week = st.selectbox("Day of the Week:", 
    options={0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"})
weather_code = st.selectbox("Weather Condition:",
    options={1:"Clear", 2:"Cloudy", 3:"Rain", 4:"Snow"})

if st.button("Predict Traffic Volume"):
    input_data = [[hour, day_of_week, weather_code]]
    prediction = model.predict(input_data)
    st.success(f"Predicted Traffic Volume: {int(prediction[0])}")

st.markdown("Built with ❤️ using Random Forest & Streamlit")
