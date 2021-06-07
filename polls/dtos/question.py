import datetime
from dataclasses import dataclass

import jsons

from polls.models import Question


@dataclass
class QuestionOutputDTO(jsons.JsonSerializable):
    questionText: str
    author: str
    status: int
    publishTime: datetime.datetime

    def __init__(self, question: Question):
        self.questionText = question.question_text
        self.author = question.author
        self.status = int(question.status)
        self.publishTime = question.pub_date


@dataclass
class QuestionInputDTO(jsons.JsonSerializable):
    questionText: str
    author: str
    status: int
    publishTime: datetime.datetime
