# AI IT Navigator - ИИ-навигация в IT-профессиях

Интеллектуальная система для помощи в выборе IT-профессии на основе персональных предпочтений и навыков пользователя.

## Описание проекта

Проект использует машинное обучение для анализа ответов пользователя на вопросы о его предпочтениях и рекомендует наиболее подходящие IT-профессии. Система также генерирует персональные рекомендации с помощью GigaChat от СБЕРа.

## Основные функции

- **Интерактивный опросник**: Ответьте на вопросы по шкале от 1 до 5
- **ML-анализ**: Алгоритм анализирует ваши ответы и определяет профиль
- **Персональные рекомендации**: Получите список подходящих профессий с процентным совпадением
- **ИИ-консультация**: GigaChat генерирует подробную мотивационную рекомендацию
- **Мотивация в School 21**: Специальные рекомендации для поступления в Школу 21 от СБЕРа

## Технологический стек

- **ML**: NumPy, кастомные алгоритмы
- **AI**: GigaChat API от СБЕРа

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd Job_choose_ml_services
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```
GIGACHAT_AUTH_KEY=your_gigachat_authorization_key
```

### 4. Запуск приложения

```bash
streamlit run app.py
```

Приложение будет доступно по адресу `http://localhost:8501`

## Структура проекта

```
Job_choose_ml_services/
├── app.py                 # Основное приложение Streamlit
├── gigachat_client.py     # Клиент для работы с GigaChat API
├── ml_logic.py           # ML-логика для анализа профилей
├── prompt_motivation.txt  # Шаблон промпта для GigaChat
├── requirements.txt      # Зависимости Python
├── .env                  # Переменные окружения
└── README.md            # Этот файл
```

## Как это работает

1. **Опрос**: Пользователь отвечает на вопросы о своих предпочтениях
2. **Анализ**: ML-алгоритм анализирует ответы и создает профиль пользователя
3. **Рекомендации**: Система подбирает подходящие профессии
4. **ИИ-консультация**: GigaChat генерирует персональные рекомендации с мотивацией

## Конфигурация

### GigaChat API

Для работы с GigaChat необходимо:

1. Получить авторизационный ключ в [GigaChat](https://developers.sber.ru/docs/ru/gigachat/quickstart/main)
2. Добавить ключ в файл `.env`

### Настройка промпта

Промпт для GigaChat находится в файле `prompt_motivation.txt`. Вы можете изменить его для настройки стиля рекомендаций.

## Использование в backend-проектах

### API интеграция

Вы можете интегрировать ML-логику в другие проекты:

```python
from ml_logic import calculate_profile, recommend
from gigachat_client import generate_personalized_text

# Получение рекомендаций
answers = [5, 4, 3, 5, 4]  # Ответы пользователя
profile = calculate_profile(answers)
results = recommend(profile)

# Генерация персонализированного текста
formatted_results = [f"{profession} ({score*100:.1f}%)"
                     for profession, score in results]
explanation = generate_personalized_text(profile, formatted_results)
```

### Конфигурация для продакшена

Для использования в production:

1. **Переменные окружения**:

```bash
GIGACHAT_AUTH_KEY=your_production_key
```

2. **Модификация промпта**:

- Отредактируйте `prompt_motivation.txt` под ваши требования
- Измените плейсхолдеры при необходимости
- Адаптируйте стиль под ваш бренд

3. **Кэширование**:

```python
# Рекомендуется кэшировать результаты для одинаковых профилей
import functools

@functools.lru_cache(maxsize=100)
def cached_recommendations(answers_tuple):
    return recommend(calculate_profile(list(answers_tuple)))
```
