import streamlit as st
from ml_logic import QUESTIONS, calculate_profile, recommend

st.set_page_config(page_title="AI IT Navigator", page_icon="🚀")

st.title("ИИ-навигация в ИТ-профессиях")
st.write("Ответьте на вопросы по шкале от 1 до 5")

answers = []

for i, (question, _) in enumerate(QUESTIONS):
    answer = st.slider(
        f"{i+1}. {question}",
        1, 5, 3
    )
    answers.append(answer)

if st.button("Получить рекомендации"):
    profile = calculate_profile(answers)
    results = recommend(profile)

    st.subheader("🎯 Вам больше всего подходят:")

    for profession, score in results:
        st.write(f"**{profession}** — совпадение {round(score*100, 1)}%")

    st.subheader("📊 Ваш профиль:")
    st.json(profile)
