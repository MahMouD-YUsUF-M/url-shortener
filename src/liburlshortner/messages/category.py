from typing import List

from liburlshortner.messages.common import ResponseBaseModel
from libutil.util import BaseModel


class Category(BaseModel):
    code: str
    label: str


class GetCategoriesResponse(ResponseBaseModel):
    data: List[Category]
