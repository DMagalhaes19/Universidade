from models.rented import rented

class season:
    def __init__(self,season,episode_number,episode_name):
        self.season = season
        self.episode_number = episode_number
        self.episode_name = episode_name
        self.state = 0
    
    def get_season(self):
        return self.season
    
    def get_episode_number(self):
        return self.episode_number
    
    def set_episode_None(self):
        self.episode_number = None
        self.episode_name = None

    def set_season(self,season,episode_number,episode_name):
        self.season = season
        self.episode_number = episode_number
        self.episode_name = episode_name
    
    def check_state(self):
        return self.status
    
    def set_state(self):
        if self.episode_number != None:
            rented.set_state(self,self.episode_number,self.episode_name)
        else:
            self.state += 1
    
    def check_episode_status(self):
        rented.check_state(self)