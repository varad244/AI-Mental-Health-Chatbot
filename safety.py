# safety.py

def is_crisis(text):
    crisis_keywords = [

        # Direct suicidal intent
        "kill myself",
        "commit suicide",
        "suicide",
        "end my life",
        "take my life",
        "want to die",
        "i want to die",
        "i am going to die",
        "i plan to die",

        # Self-harm behaviors
        "hurt myself",
        "self harm",
        "self-harm",
        "cut myself",
        "cutting myself",
        "burn myself",
        "harm myself",
        "i deserve pain",

        # Hopelessness / giving up
        "give up on life",
        "life is pointless",
        "no reason to live",
        "nothing matters anymore",
        "i am done with life",
        "i can't go on",
        "i can't continue",

        # Passive death wishes
        "i wish i was dead",
        "i don't want to live anymore",
        "i wish i wouldn't wake up",
        "better off dead",
        "everyone would be better without me",

        # Extreme emotional distress
        "i feel empty inside",
        "i feel completely broken",
        "i am a burden",
        "i hate myself",
        "i am worthless"
    ]

    text = text.lower()
    return any(keyword in text for keyword in crisis_keywords)


def crisis_response():
    """
    Returns a safe, empathetic response with professional help resources.
    """

    return (
        "I'm really sorry that you're feeling this way. "
        "You're not alone, and your life matters.\n\n"
        "I can't help with this directly, but I strongly encourage you "
        "to reach out to someone who can support you right now.\n\n"
        "📞 Mental Health Helplines (India):\n"
        "- AASRA: +91-9820466726\n"
        "- KIRAN (24/7): 1800-599-0019\n\n"
        "If you are outside India, please contact your local emergency number "
        "or a trusted person immediately."
    )
