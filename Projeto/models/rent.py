class rent:
    def __init__(self,ID_client,ID_series,num_season,num_episode):
        self.client = ID_client
        self.series = ID_series
        self.season = num_season
        self.episode = num_episode
    
    def get_client(self):
        return self.client
    
    def get_series(self):
        return self.series
    
    def get_season(self):
        return self.season
    
    def get_episode(self):
        return self.episode