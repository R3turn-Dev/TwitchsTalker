from dataclasses import dataclass
from typing import Optional
from asyncio import StreamReader, StreamWriter

class Handler:
    @staticmethod
    def listener():
        def decorator(func):
            func()
        return decorator


class User:
    def __init__(
            self,
            username,
            display_name: Optional[str] = "",
            uid: int = 0
            ):
        self.username = username
        self.display_name = display_name or username
        self.uid = uid


class Chatter(User):
    def __init__(self, *args, channel: str = "", **kwargs):
        super().__init__(*args, **kwargs)
        self.channel = channel

    @staticmethod
    def make_chatter(user: User, channel: str = ""):
        return Chatter()


@dataclass
class Context:
    reader: StreamReader
    writer: StreamWriter
    mode: str
    user: str
    channel: str
    message: str

    @property
    def author(self):
        return Chatter.make_chatter(User(self.user), self.channel)

    async def send(self, msg):
        self.writer.write((msg + "\r\n").encode())

    async def reply(self, msg):
        msg = f"@{self.user} " + msg
        await self.send(f"PRIVMSG #{self.channel} :{msg}")
