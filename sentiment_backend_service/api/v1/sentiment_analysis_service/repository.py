import gdown
import requests
from sentiment_backend_service.settings import ip
from sentiment_backend_service.api.v1.sentiment_analysis_service.sentiment_analyzer.model import model
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse


def request_list():
    url = f"http://{ip}:8000/v1/sentiment_backend/analysis_service/comments"
    r = requests.get(url=url)
    data = r.json()
    results = []
    for i in data:
        results.append(i)
        sentiment, confidence, probabilities = model.predict(i['comment'])
        i['prediction'] = SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)
    return results


def download():
    gdown.download(
        "https://drive.google.com/uc?id=1V8itWtowCYnb2Bc9KlK9SxGff9WwmogA",
        "sentiment_backend_service/api/v1/sentiment_analysis_service/assets/model_state_dict.bin",
    )
    return "Model downloaded successfully"


def predict(request: SentimentRequest):
        sentiment, confidence, probabilities = model.predict(request.text)
        return SentimentResponse(sentiment=sentiment, confidence=confidence, probabilities=probabilities)
