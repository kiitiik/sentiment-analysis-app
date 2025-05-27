import streamlit as st
from sentiment import predict_sentiment

st.set_page_config(page_title="Анализ Тональности", layout="centered")

st.title("Анализ Тональности Текста")
st.write("Введите текст, и модель определит его эмоциональную окраску.")

user_input = st.text_area("Ваш текст", height=200)

if st.button("Анализировать"):
    if user_input.strip():
        result = predict_sentiment(user_input)
        st.success(f"Результат: **{result}**")
    else:
        st.warning("Пожалуйста, введите текст.")
