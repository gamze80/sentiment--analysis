import requests
from sentiment_backend_service.api.v1.sentiment_analysis_service.sentiment_analyzer.model import model
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse
from sentiment_backend_service.settings import ip


class AnalysisRepository:
    def predict(request:SentimentRequest ):
        sentiment, confidence, probabilities = model.predict(request.text)
        return SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)

    def request_list(x:None):
        url = f"http://{ip}:8000/v1/sentiment_backend/analysis_service/comments"
        r = requests.get(url=url)
        data = r.json()
        results = []
        for i in data:
            results.append(i)
            sentiment, confidence, probabilities = model.predict(i['comment'])
            i['prediction'] = SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)
        return results
