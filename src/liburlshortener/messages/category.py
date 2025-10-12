from typing import List

from liburl_shortener.messages.common import ResponseBaseModel
from libutil.util import BaseModel


class Category(BaseModel):
    code: str
    label: str


class GetCategoriesResponse(ResponseBaseModel):
    data: List[Category]
