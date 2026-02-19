import streamlit as st
from ml_logic import QUESTIONS, calculate_profile, recommend
from gigachat_client import generate_personalized_text

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

    formatted_results = []
    for profession, score in results:
        percent = round(score * 100, 1)
        st.write(f"**{profession}** — совпадение {percent}%")
        formatted_results.append(f"{profession} ({percent}%)")

    st.subheader("🤖 Персональная рекомендация")

    with st.spinner("Генерируем персональный разбор..."):
        explanation = generate_personalized_text(profile, formatted_results)

    st.write(explanation)