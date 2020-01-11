from datetime import datetime

from .user import User

from typing import Optional


class Member(User):
    """Twitch Member Model (child class of :class:`User`)

    :class:`Member` model is often used in watching situation.

    Attributes
    ----------
    streamer: :class:`User`
        Twitch User who the member is watching or chatting for
    followed_at: :class:`datetime`
        The follow-starting date of the member
    """
    def __init__(self, *args, **kwargs):
        if "streamer" not in kwargs:
            raise ValueError("Streamer object must be included when initializing a Member")

        self.streamer: User = kwargs.pop("streamer")
        self.followed_at: datetime = kwargs.pop("followed_at", datetime(1970, 1, 1))

        super().__init__(*args, **kwargs)

