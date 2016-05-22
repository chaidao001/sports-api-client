import requests

from utils.sessionmanager import SessionManager


class Operation:
    def __init__(self, endpoint: str, session_manager: SessionManager):
        self._endpoint = endpoint
        self._session_manager = session_manager

    def _call_api(self, headers, data):
        req = requests.post(self._endpoint, headers=headers, data=data)
