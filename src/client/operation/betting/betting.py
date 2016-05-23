from client.operation.operation import Operation
from utils.configs import Configs
from utils.sessionmanager import SessionManager


class Betting(Operation):
    def __init__(self, configs: Configs, session_manager: SessionManager):
        super().__init__(configs.betting_endpoint, session_manager)

    def place_orders(self, market_id: str, instructions: list(), customer_ref: str = None):
        pass

    def cancel_orders(self, market_id: str = None, instruction: list() = None, customer_ref: str = None):
        pass

    def replace_orders(self, market_id: str, instructions: list(), customer_ref: str = None):
        pass

    def update_orders(self, market_id: str, instructions: list(), customer_ref: str = None):
        pass
