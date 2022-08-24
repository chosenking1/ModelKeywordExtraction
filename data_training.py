import dateutil
from pydantic import BaseModel, dataclasses
from pydantic.datetime_parse import datetime


class KeywordExtraction(BaseModel):
    title: str
    # price : int
    abstract: str
    paper_text: str

