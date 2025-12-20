# openai_client.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(user_input, mood):
    """
    Generates a mental health supportive response using OpenAI.
    """

    system_prompt = f"""
    You are a compassionate mental health support chatbot.

    The user's emotional state is: {mood}

    Rules:
    - Be empathetic and calm
    - Offer practical coping suggestions
    - Do NOT give medical or legal advice
    - Do NOT encourage self-harm
    - Keep the response supportive and concise
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
