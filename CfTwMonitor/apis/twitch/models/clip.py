from .base import TwitchModelBase

from datetime import datetime

from typing import Optional


class Clip(TwitchModelBase):
    def __init__(self,
                 id: int,
                 url: str,
                 embed_url: str,
                 broadcaster_id: int,
                 broadcaster_name: str,
                 creator_id: int,
                 creator_name: str,
                 video_id: int,
                 language: str,
                 title: str,
                 view_count: int,
                 created_at: datetime,
                 thumbnail_url: str,
                 game_id: Optional[int] = 0,
                 *args, **kwargs):
        self.id = int(id)
        self.url = url
        self.embed_url = embed_url
        self.broadcaster_id = int(broadcaster_id)
        self.broadcaster_name = broadcaster_name
        self.creator_id = int(creator_id)
        self.creator_name = creator_name
        self.video_id = int(video_id)
        self.game_id = int(game_id)
        self.language = language
        self.title = title
        self.view_count = view_count
        self.created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        self.thumbnail_url = thumbnail_url

        super().__init__()
