import numpy as np

# 7 скрытых шкал
SCALES = [
    "analytical",
    "systemic",
    "communication",
    "creativity",
    "attention_to_detail",
    "data_interest",
    "stress_resilience"
]

# 21 вопрос (по 3 на каждую шкалу)
QUESTIONS = [
    # Analytical
    ("Мне нравится искать закономерности в сложной информации.", "analytical"),
    ("Мне интересно разбираться, как устроены сложные системы.", "analytical"),
    ("Я люблю задачи, где нужно продумывать логику шаг за шагом.", "analytical"),

    # Systemic
    ("Мне важно понимать всю систему целиком, а не только её часть.", "systemic"),
    ("Мне комфортно структурировать процессы и наводить порядок.", "systemic"),
    ("Я люблю планировать действия заранее.", "systemic"),

    # Communication
    ("Мне нравится координировать людей и договариваться.", "communication"),
    ("Я легко объясняю сложные вещи другим.", "communication"),
    ("Мне интересно понимать потребности других людей.", "communication"),

    # Creativity
    ("Мне нравится придумывать новые идеи и решения.", "creativity"),
    ("Мне важна визуальная эстетика и дизайн.", "creativity"),
    ("Я люблю нестандартные задачи.", "creativity"),

    # Attention to detail
    ("Я часто замечаю ошибки, которые пропускают другие.", "attention_to_detail"),
    ("Мне нравится проверять работу на наличие неточностей.", "attention_to_detail"),
    ("Я люблю доводить результат до идеала.", "attention_to_detail"),

    # Data interest
    ("Мне интересно работать с числами и статистикой.", "data_interest"),
    ("Мне нравится анализировать данные и строить выводы.", "data_interest"),
    ("Я получаю удовольствие от исследования больших объёмов информации.", "data_interest"),

    # Stress resilience
    ("Я спокойно реагирую на срочные задачи.", "stress_resilience"),
    ("Мне комфортно работать в условиях неопределённости.", "stress_resilience"),
    ("Я чувствую ответственность за результат команды.", "stress_resilience"),
]

# Профили профессий (веса по шкалам от 0 до 1)
PROFESSIONS = {
    "Проджект-менеджер": {
        "analytical": 0.6,
        "systemic": 0.8,
        "communication": 1.0,
        "creativity": 0.5,
        "attention_to_detail": 0.6,
        "data_interest": 0.4,
        "stress_resilience": 0.9,
    },
    "UX/UI – дизайн": {
        "analytical": 0.5,
        "systemic": 0.4,
        "communication": 0.7,
        "creativity": 1.0,
        "attention_to_detail": 0.8,
        "data_interest": 0.3,
        "stress_resilience": 0.4,
    },
    "Биоинформатика": {
        "analytical": 1.0,
        "systemic": 0.7,
        "communication": 0.3,
        "creativity": 0.5,
        "attention_to_detail": 0.8,
        "data_interest": 1.0,
        "stress_resilience": 0.6,
    },
    "Разработчик ПО": {
        "analytical": 0.9,
        "systemic": 0.8,
        "communication": 0.4,
        "creativity": 0.6,
        "attention_to_detail": 0.7,
        "data_interest": 0.6,
        "stress_resilience": 0.7,
    },
    "Data Scientist": {
        "analytical": 1.0,
        "systemic": 0.6,
        "communication": 0.4,
        "creativity": 0.7,
        "attention_to_detail": 0.8,
        "data_interest": 1.0,
        "stress_resilience": 0.6,
    },
    "DevOps / SRE": {
        "analytical": 0.8,
        "systemic": 1.0,
        "communication": 0.4,
        "creativity": 0.4,
        "attention_to_detail": 0.9,
        "data_interest": 0.7,
        "stress_resilience": 1.0,
    },
    "Кибербезопасность": {
        "analytical": 0.9,
        "systemic": 0.7,
        "communication": 0.3,
        "creativity": 0.4,
        "attention_to_detail": 1.0,
        "data_interest": 0.8,
        "stress_resilience": 0.8,
    },
    "QA-инженер": {
        "analytical": 0.7,
        "systemic": 0.6,
        "communication": 0.5,
        "creativity": 0.3,
        "attention_to_detail": 1.0,
        "data_interest": 0.5,
        "stress_resilience": 0.7,
    },
    "Бизнес- и системный аналитик": {
        "analytical": 0.9,
        "systemic": 0.8,
        "communication": 0.8,
        "creativity": 0.5,
        "attention_to_detail": 0.7,
        "data_interest": 0.7,
        "stress_resilience": 0.6,
    },
}


def calculate_profile(answers):
    scale_scores = {scale: [] for scale in SCALES}

    for answer, (_, scale) in zip(answers, QUESTIONS):
        scale_scores[scale].append(answer)

    profile = {scale: np.mean(values) / 5 for scale, values in scale_scores.items()}
    return profile


def cosine_similarity(vec1, vec2):
    v1 = np.array(list(vec1.values()))
    v2 = np.array(list(vec2.values()))
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def recommend(profile, top_n=3):
    scores = {}

    for profession, weights in PROFESSIONS.items():
        scores[profession] = cosine_similarity(profile, weights)

    sorted_professions = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_professions[:top_n]
