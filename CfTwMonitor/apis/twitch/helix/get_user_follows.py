from datetime import datetime

from .base import ApiBase
from .. import User, Member

from .tools.id_and_logins import IdLoginParser

from typing import Union, List, Dict


class GetUserFollows(ApiBase):
    url = ApiBase.url + "users/follows"

    # TODO: Support pagination
    async def perform(self,
                      from_id: Union[str, User, Member],
                      to_id: Union[str, User, Member]):
        from_id = ("from_id", IdLoginParser.make_user_id(from_id)[0])
        to_id = ("to_id", IdLoginParser.make_user_id(to_id)[0])

        resp = await self.perform_get([
            from_id,
            to_id,
            ("first", 100),
        ])

        token = resp["pagination"]
        total = resp["total"]

        data: List[Dict[str, Union[int, str, datetime]]] = []

        for user in resp["data"]:
            user["from_id"] = int(user["from_id"])
            user["to_id"] = int(user["to_id"])

            user["followed_at"] = datetime.strptime(user["followed_at"], "%Y-%m-%dT%H:%M:%SZ")
            data.append(user)

        return total, token, data
