class StartupInfo:
    def __init__(self):
        self._item = None
        self._status = None
        self._time = None

    def getItem(self):
        return self._item

    def setItem(self, item):
        self._item = item

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def getTime(self):
        return self._time

    def setTime(self, time):
        self._time = time
