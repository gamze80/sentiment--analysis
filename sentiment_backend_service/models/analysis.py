from typing import Dict
import json
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from .helper import OrmHelper

from pydantic import BaseModel

Base = declarative_base()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


class Prediction(Base):
    __tablename__ = 'Predictions'
    __table_args__ = {'comment': 'prediction'}

    comment_text: str = Column(String, primary_key=True)
    comment_prediction: str = Column(String, primary_key=True)

    def __repr__(self) -> str:
        return json.dumps(self.dict())

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return OrmHelper.toDict(self)
