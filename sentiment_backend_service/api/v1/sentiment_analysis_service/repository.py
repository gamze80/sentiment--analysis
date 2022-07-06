from sentiment_backend_service.api.v1.sentiment_analysis_service.sentiment_analyzer.model import model
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse
import requests


class AnalysisRepository:
    def predict(request:SentimentRequest ):
        sentiment, confidence, probabilities = model.predict(request.text)
        return SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)


    def request_list(input_site:str):
        url = input_site
        r = requests.get(url=url)
        data = r.json()
        results = []
        for i in data:
            results.append(i)
            sentiment, confidence, probabilities = model.predict(i['comment'])
            i['prediction'] = SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)
        return results


