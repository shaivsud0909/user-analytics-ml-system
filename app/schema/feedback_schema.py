from pydantic import BaseModel, Field
from typing import Optional


class FeedbackRequest(BaseModel):

    is_correct: bool

    rating: Optional[int] = Field(
        default=None,
        ge=1,
        le=5
    )