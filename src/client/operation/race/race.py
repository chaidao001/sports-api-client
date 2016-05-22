from client.operation.operation import Operation


class Race(Operation):
    def __init__(self, configs, session_manager):
        super().__init__(configs.scores_endpoint, session_manager)

    def list_race_details(self):
        pass
