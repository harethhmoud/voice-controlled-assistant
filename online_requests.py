import wikipedia
import speech
import requests
import pywhatkit


def wiki_search(query):
    results = wikipedia.summary(query, sentences=2)
    return results


def get_news():
    news_headlines = []
    results = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=b6580091b81a44558d69631419c31783"
                           "+&category=general").json()
    articles = results["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def google_search(topic):
    pywhatkit.search(topic)


def youtube_search(search):
    pywhatkit.playonyt(search)


def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(number, message)