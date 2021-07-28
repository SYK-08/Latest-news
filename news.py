import config
import requests
import pyttsx3

def headlines():
    endpoint = "https://newsapi.org/v2/top-headlines"
    
    query_params = {
        "source": "bbc-news",
        "language": "en",
        "apiKey": config.api_key,
        "page_size": 10,
        "sortBy": "top"
    }

    res = requests.get(endpoint, params=query_params)
    open_page = res.json() #Converted to .json
    article = open_page["articles"]

    results = []

    for ar in article:
        # results.append(ar["description"])
        results.append(ar["title"])
    
    for i in range(len(results)):
        print(i+1, results[i])

    engine = pyttsx3.init("espeak")
    engine.say(results)
    speed = engine.getProperty('rate')
    engine.setProperty('rate', 190)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    headlines()