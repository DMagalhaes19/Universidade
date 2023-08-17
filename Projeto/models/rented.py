class rented:
    def __init__(self,episode_number,episode_name):
        self.episode_number = episode_number
        self.episode_name = episode_name
        self.state = 0
    
    def check_state(self):
        return self.state 
        
    def set_state(self,episode_number,episode_name):
        self.state =    1 #0 para não alugado e 1 para alugada
        self.episode_number = episode_number
        self.episode_name = episode_name
    
    def set_episode(self,episode_number,episode_name):
        self.episode_number = episode_number
        self.episode_name = episode_name
    
    def get_episode_number(self):
        return self.episode_number