import inspect
import asyncio
from .errors import InvalidArgumentTypeError


class Task:
    def __init__(
            self,
            func,
            seconds: float = .0,
            minutes: float = .0,
            hours: float = .0
            ):
        if not inspect.iscoroutinefunction(func):
            raise InvalidArgumentTypeError(func, "coroutine")

        self.func = func
        self.interval = seconds + (minutes * 60.0) + (hours * 3600.0)


    @staticmethod
    def loop(*, seconds=0, minutes=0, hours=0):
        def decorator(func):
            return Task(func, seconds, minutes, hours)

        return decorator


class TwitchDownloadTask:
    def __init__(self, channel, interval=5.0):
        self.channel = channel
        self.interval = interval


    @property
    def uri(self):
        return "https://twitch.tv/" + self.channel

    @Task.loop(seconds=5.0)
    async def check(self):

