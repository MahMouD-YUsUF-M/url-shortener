from typing import Optional, List, Union

from libutil.util import BaseModel
from pydantic import Field


class ResponseBaseModel(BaseModel):
    success: bool
    code: int = 200
    message: Optional[str] = Field(default_factory=str)
    data: Union[dict, List[dict]] = Field(default_factory=dict)


class ErrorResponse(ResponseBaseModel):
    success: bool = False
    code: int
    traceback: Optional[list[str]] = None
