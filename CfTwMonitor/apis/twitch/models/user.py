from .base import TwitchModelBase

from typing import Optional


class User(TwitchModelBase):
    """Twitch User Model

    Attributes
    ----------
    id: :class:`int`
        Users's ID
    login: :class:`str`
        User's login name
    display_name: :class:`str`
        User's display name
    type: :class:`str`
        User's type in "staff", "admin", "global_mod", or "" for default
    broadcaster_type: :class:`str`
        User's broadcaster type in "partner", "affiliate", or "" for default
    description: :class:`str`
        User's channel description
    profile_image_url: :class:`str`
        URL of the User's offline image
    offline_image_url: :class:`str`
        URL of the User's profile image
    view_count: :class:`int`
        Total number of views of the User's channel
    email: :class:`Optional[str]`
        User's email address. Returned if the request includes the 'user:read:email' scope.
    """
    def __init__(self,
                 id: int,
                 login: str,
                 display_name: str,
                 type: str,
                 broadcaster_type: str,
                 description: str,
                 profile_image_url: str,
                 offline_image_url: str,
                 view_count: int = 0,
                 email: Optional[str] = None):
        # Required
        self._id = int(id)
        self.login = login
        self.display_name = display_name

        # User types
        self._type = type
        self.broadcaster_type = broadcaster_type

        # Profile Info
        self.description = description
        self.profile_image_url = profile_image_url
        self.offline_image_url = offline_image_url

        # Optional
        self.view_count = view_count
        self.email = email

        super().__init__()

    def __str__(self):
        return self.login

    @property
    def id(self):
        return self._id

