import requests

class API:
    def __init__(self):
        self.url = "https://sentiment-by-api-ninjas.p.rapidapi.com/v1/sentiment"
        self.headers = {
            "x-rapidapi-key": "6a6406b76emshc3b25cb812859b4p1addd1jsn1f16b46554eb",
            "x-rapidapi-host": "sentiment-by-api-ninjas.p.rapidapi.com"
        }
    
    def sentiment_analysis(self, text):
        querystring = {"text": text}
        response = requests.get(self.url, headers=self.headers, params=querystring)
        return response.json()