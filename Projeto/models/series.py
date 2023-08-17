from models.season import season

class series:
    def __init__(self,id:int,name,num_temp,num_epis,name_epis):
        self.name_series = name
        self.id = id
        self.status = 0
        season.__init__(self,num_temp,num_epis,name_epis)
    
    def get_series_name(self)->object:
        return self.name_series
            
    def get_ID(self)->object:
        return self.id

    def get_season(self):
        return season.get_season(self)

    def get_episode_number(self):
        return season.get_episode_number(self)

    def get_status(self):
        return self.status

    def set_series(self,season_number,episode_number,episode_name):
        season.set_season(self,season_number,episode_number,episode_name)
    
    def set_season_none(self):
        season.set_episode_None(self)
    
    def see_season_status(self):
        season.check_state(self)
    
    def change_season_status(self):
        season.set_state(self)
    
    def rent_series(self):
        self.status += 1
    
    def see_episode_status(self):
        season.check_episode_status(self)
    
    def change_episode_status(self):
        season.set_state(self)