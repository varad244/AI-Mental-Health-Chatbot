from textblob import TextBlob

def detect_mood(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.6:
        return "Sad"
    elif -0.6 <= polarity < -0.2:
        return "Anxious"
    else:
        return "Neutral"

