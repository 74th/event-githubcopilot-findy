from typing import Optional, TypedDict


from datetime import datetime

class Task(TypedDict):
    id: Optional[int]
    text: str
    done: bool
    created_at: Optional[datetime]
    completed_at: Optional[datetime]
