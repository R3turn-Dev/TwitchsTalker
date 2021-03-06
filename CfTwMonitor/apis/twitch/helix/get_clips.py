from .base import ApiBase
from .. import User, Clip

from typing import Union, List


class GetClips(ApiBase):
    url: str = ApiBase.url + "clips"

    auth_require = {"client_id"}
    parameters = {"id", "game_id", "broadcaster_id"}

    async def perform(self,
                      ids: Union[int, str, User, List[Union[int, str, User]]] = None,
                      broadcaster_id: Union[int, str, User] = None,
                      *args, **kwargs
                      ):
        """
        clip ids 를 통한 조회 or broadcaster_id 를 통한 clips 조회
        """

        if ids:  # Clip ids
            if not isinstance(ids, list):
                ids = [('id', ids)]
            else:
                ids = [('id', x) for x in ids]

            parameters = ids.copy()
            parameters.extend(args)
            data = await self.perform_get(parameters)
        else:
            if isinstance(broadcaster_id, str):
                broadcaster_id = int(broadcaster_id)
            elif isinstance(broadcaster_id, User):
                broadcaster_id = broadcaster_id.id

            parameters = [('broadcaster_id', broadcaster_id)]
            parameters.extend(args)
            data = await self.perform_get(parameters)

        """
        {
            "data": [
                {
                    "id":"RandomClip1",
                    "url":"https://clips.twitch.tv/AwkwardHelplessSalamanderSwiftRage",
                    "embed_url":"https://clips.twitch.tv/embed?clip=RandomClip1",
                    "broadcaster_id":"1234",
                    "broadcaster_name": "JJ",
                    "creator_id":"123456",
                    "creator_name": "MrMarshall",
                    "video_id":"1234567",
                    "game_id":"33103",
                    "language":"en",
                    "title":"random1",
                    "view_count":10,
                    "created_at":"2017-11-30T22:34:18Z",
                    "thumbnail_url":"https://clips-media-assets.twitch.tv/157589949-preview-480x272.jpg"
                },
                ...
            ],
            "pagination": {
                "cursor": "eyJiIjpudWxsLCJhIjoiIn0"
            }
        }
        """

        returns: List[Clip] = []
        for clip in data["data"]:
            returns.append(Clip(**clip))

        return returns
