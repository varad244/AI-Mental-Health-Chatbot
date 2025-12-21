#api key test
from openai_client import generate_response

print(generate_response(
    "I feel anxious about my career and future",
    "Anxious"
))

#saftey test
from safety import is_crisis, crisis_response

print(is_crisis("I feel like giving up on life"))
print(is_crisis("I am stressed about exams"))

if is_crisis("I want to die"):
    print(crisis_response())



# Checking the mood detector code correctly working or not 
from textblob import TextBlob

def senti(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.6:
        return "Sad"
    elif -0.6 <= polarity < -0.2:
        return "Anxious"
    else:
        return "Neutral"


text = "The food there was not really delicious"
print(senti(text))
