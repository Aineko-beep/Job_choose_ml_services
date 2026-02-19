import json
import os
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

def generate_personalized_text(profile, recommendations):
    with open('prompt_motivation.txt', 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    
    prompt = prompt_template.format(
        profile_json=json.dumps(profile, ensure_ascii=False, indent=2),
        recommendations=recommendations
    )

    try:
        giga = GigaChat(
            credentials=os.getenv("GIGACHAT_AUTH_KEY"),  
            model="GigaChat:latest",                    
            verify_ssl_certs=False
        )

        response = giga.chat(prompt)
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
