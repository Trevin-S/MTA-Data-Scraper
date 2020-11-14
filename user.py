class User():
 
    def __init__(self):
        self.username = read(open("username.txt", "r"))
        self.password = read(open("password.txt", "r"))
        self.paused = False
        self.lastState = False
        self.running = True
 
    def get_username(self):
        return self.username
 
    def get_password(self):
        return self.password
 
    def pause(self, state):
        self.paused = state
 
    def is_paused(self):
        return self.paused
 
    def get_last_state(self):
        return self.lastState
 
    def last_state(self, state):
        self.lastState = state
 
    def is_running(self):
        return self.running
 
    def stop_running(self):
        self.running = False