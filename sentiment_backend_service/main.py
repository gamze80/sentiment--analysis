import sentiment_backend_service.settings
import uvicorn
from fastapi import FastAPI
import gdown
from sentiment_backend_service.api.v1.book_service.router import BookRouter
from sentiment_backend_service.api.v1.sentiment_analysis_service.router import AnalysisRouter

VERSION = "1.0.0"

app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
)

sub_app = FastAPI(
    title="Backend Service",
    version=VERSION,
    description="Backend service developed using fastapi",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

gdown.download(
    "https://drive.google.com/uc?id=1V8itWtowCYnb2Bc9KlK9SxGff9WwmogA",
    "sentiment_backend_service/api/v1/sentiment_analysis_service/assets/model_state_dict.bin",
)
sub_app.include_router(BookRouter().get_router(), prefix="/book_service")
sub_app.include_router(AnalysisRouter().get_router(), prefix="/analysis_service")
app.mount("/v1/sentiment_backend", sub_app)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
