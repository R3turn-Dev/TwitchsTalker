from .base import ApiBase
from .. import User, Stream

from .tools.id_and_logins import IdLoginParser

from typing import Union, List


class GetStreams(ApiBase):
    url = ApiBase.url + "streams"

    auth_require = {"client_id"}
    parameters = {"id", "login"}

    async def perform(self,
                      ids: Union[int, str, User, List[Union[int, str, User]]] = None,
                      logins: Union[str, User, List[Union[str, User]]] = None,
                      ) -> List[Stream]:
        ids = [('id', x) for x in IdLoginParser.make_user_id(ids)]
        logins = [('login', x) for x in IdLoginParser.make_user_login(logins)]

        data = await self.perform_get(ids + logins)

        # Example Response
        """
        {
            "data": [
                {
                    "id": "26007494656",
                    "user_id": "23161357",
                    "user_name": "LIRIK",
                    "game_id": "417752",
                    "type": "live",
                    "title": "Hey Guys, It's Monday - Twitter: @Lirik",
                    "viewer_count": 32575,
                    "started_at": "2017-08-14T16:08:32Z",
                    "language": "en",
                    "thumbnail_url": "https://static-cdn.jtvnw.net/previews-ttv/live_user_lirik-{width}x{height}.jpg"
                },
                    "tag_ids":  [
                        "6ea6bca4-4712-4ab9-a906-e3336a9d8039"
                    ]
                ...
            ],
            "pagination": {
                "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MjB9fQ=="
            }
        }
        """

        returns: List[Stream] = []
        for user in data["data"]:
            returns.append(Stream(**user))

        return returns
