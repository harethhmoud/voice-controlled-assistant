import speech
import open_app
import online_requests

if __name__ == "__main__":
    speech.greet_user()

    while True:
        transcript = speech.recognize()

        if 'open app' in transcript:
            speech.say("Which app would you like to open?")
            app = speech.recognize()
            open_app.opens_app(app)
            break

        if 'Wikipedia' in transcript:
            speech.say("What would you like to search?")
            search = speech.recognize()
            result = online_requests.wiki_search(search)
            speech.say(result)
            print(result)
            break

        if "read the news" in transcript:
            speech.say("I will read out the latest news")
            news = online_requests.get_news()
            for new in news:
                speech.say(new)
            break

        if "Google" in transcript:
            speech.say("What would you like me to Google?")
            topic = speech.recognize()
            online_requests.google_search(topic)
            break

        if "YouTube" in transcript:
            speech.say("What would you like to watch?")
            search = speech.recognize()
            online_requests.youtube_search(search)
            break

        if "send WhatsApp message" in transcript:
            speech.say("What would you like to send, and to who?")
            number = input("Enter the number: ")
            message = input("Enter the message: ")
            online_requests.send_whatsapp_message(number, message)
            speech.say("Done")
            break
