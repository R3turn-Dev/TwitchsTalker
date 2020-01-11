from .base import ApiBase
from .. import User

from .tools.id_and_logins import IdLoginParser

from typing import Union, List


class GetUsers(ApiBase):
    url: str = ApiBase.url + "users"

    auth_require = {"client_id"}
    parameters = {"id", "login"}

    async def perform(self,
                      ids: Union[int, str, User, List[Union[int, str, User]]] = None,
                      logins: Union[str, User, List[Union[str, User]]] = None,
                      ):
        ids = [('id', x) for x in IdLoginParser.make_user_id(ids)]
        logins = [('login', x) for x in IdLoginParser.make_user_login(logins)]

        data = await self.perform_get(ids + logins)

        # Example Response
        """
        {
            "data": [{
                "id": "44322889",
                "login": "dallas",
                "display_name": "dallas",
                "type": "staff",
                "broadcaster_type": "",
                "description": "Just a gamer playing games and chatting. :)",
                "profile_image_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/dallas-profile_image-1a2c906ee2c35f12-300x300.png",
                "offline_image_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/dallas-channel_offline_image-1a2c906ee2c35f12-1920x1080.png",
                "view_count": 191836881,
                "email": "login@provider.com"
            }]
        }
        """

        returns: List[User] = []
        for user in data["data"]:
            returns.append(User(**user))

        return returns
