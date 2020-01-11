from datetime import datetime


class TwitchModelBase:
    def __init__(self):
        self._model_created_date: datetime = datetime.now()
