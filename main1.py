from textblob import TextBlob

def analyze_sentiment(text):
    blob =TextBlob(text)
    sentiment_score=blob.sentiment.polarity
    if sentiment_score > 0:
        return "positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Netural"
    
value="Wow it's car"
print("Sentiment:",analyze_sentiment(post))