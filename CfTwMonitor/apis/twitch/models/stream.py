from .base import TwitchModelBase

from datetime import datetime

from typing import Optional


class Stream(TwitchModelBase):
    def __init__(self,
                 id: int,
                 user_id: int,
                 user_name: str,
                 game_id: Optional[int],
                 title: str,
                 type: str,
                 viewer_count: int,
                 started_at: datetime,
                 language: str,
                 thumbnail_url: str,
                 *args, **kwargs):
        self.id = int(id)
        self.user_id = int(user_id)
        self.user_name = user_name
        self.game_id = int(game_id)
        self.title = title
        self.viewer_count = viewer_count
        self.started_at = datetime.strptime(started_at, "%Y-%m-%dT%H:%M:%SZ")
        self.language = language
        self.thumbnail_url = thumbnail_url

        super().__init__()
