from ...models.user import User

from typing import Union, List


class IdLoginParser:
    @classmethod
    def make_user_id(cls, obj: Union[int, str, User, List[Union[int, str, User]]]) -> list:
        if obj is None:
            return []
        elif isinstance(obj, User):
            return [obj.id]
        elif isinstance(obj, list):
            return [cls.make_user_id(x)[0] for x in obj]
        elif isinstance(obj, int):
            return [str(obj)]
        else:
            return obj

    @classmethod
    def make_user_login(cls, obj: Union[str, User]) -> list:
        if obj is None:
            return []
        elif isinstance(obj, User):
            return [obj.login]
        elif isinstance(obj, list):
            return [cls.make_user_login(x)[0] for x in obj]
        else:
            return [obj]

