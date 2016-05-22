from client.operation.operation import Operation
from utils.configs import Configs
from utils.sessionmanager import SessionManager


class Betting(Operation):
    def __init__(self, configs: Configs, session_manager: SessionManager):
        super().__init__(configs.betting_endpoint, session_manager)

    def list_market_profit_and_loss(self):
        pass

    def list_current_orders(self):
        pass

    def list_cleared_orders(self):
        pass

    def place_orders(self):
        pass

    def cancel_orders(self):
        pass

    def replace_orders(self):
        pass

    def update_orders(self):
        pass
