from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId

@dataclass(frozen=True)
class User:
    email: str
    password: str
    _id: ObjectId = ObjectId
    creation_date: datetime = datetime.now()

    def __post_init__(self):
        if self._id is None:
            self._id = ObjectId()