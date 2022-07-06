from sentiment_backend_service.interfaces.generic_router import GenericRouter
from sentiment_backend_service.models.analysis import SentimentRequest, SentimentResponse
from .repository import AnalysisRepository
from . import test



class AnalysisRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind_routes()

    def bind_routes(self):
        self.get_router().post("/predict_text", response_model=SentimentResponse, tags=["Predictions"])(self.predict)
        self.get_router().post("/predict_list", response_model=SentimentResponse, tags=["Predictions"])(
            self.request_list)
        self.get_router().get("/comments", tags=["Test List Of Comments"])(test.comment)

    def predict(self,
                request: SentimentRequest):
        return AnalysisRepository.predict(request)

    def request_list(self
                     , input_site: str):
        return AnalysisRepository.request_list(input_site)
