from client.operation.operation import Operation


class MarketInfo(Operation):
    def __init__(self, configs, session_manager):
        super().__init__(configs.betting_endpoint, session_manager)

    def list_event_types(self):
        pass

    def list_competitions(self):
        pass

    def list_time_ranges(self):
        pass

    def list_events(self):
        pass

    def list_market_types(self):
        pass

    def list_countries(self):
        pass

    def list_venues(self):
        pass

    def list_market_catalogue(self):
        pass

    def list_market_book(self):
        pass
