from client.operation.operation import Operation


class Account(Operation):
    def __init__(self, configs, session_manager):
        super().__init__(configs.account_endpoint, session_manager)

    def get_account_funds(self):
        pass

    def get_account_details(self):
        pass

    def get_account_statement(self):
        pass
