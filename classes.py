class user():
 
    def __init__(self):
        self.username = 'user'
        self.passFile = open("password.txt", "r")
        self.password = self.passFile.read()
        self.paused = False
        self.lastState = False
        self.running = True

        self.passFile.close()  
 
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
 
class titleAgencies:
 
    def __init__(self):
        self.titleAgenciesLong = []
        self.titleAgenciesShort = []

    def get_title_agencies(self):
        return self.titleAgenciesShort
 
    def add_long_agency(self, agency):
        self.titleAgenciesLong.append(agency)
 
    def add_short_agency(self, agency):
        self.titleAgenciesShort.append(agency)
 
    def agency_count(self):
        return len(self.titleAgenciesLong)
 
    def short_agency(self, index, start = None, end = None):
        return self.titleAgenciesShort[index][start:end]
 
    def long_agency(self, index, start = None, end = None):
        return self.titleAgenciesLong[index][start:end]
 
class agent:
 
    deals = []
 
    def __init__(self): 
        self.dealCount = 0
        self.full = False
        agent.clear_deals()
 
    def add_deal(self, titleName, listingSide, MS1, buySide, MS2): 
        self.new_deal = [titleName, listingSide, MS1, buySide, MS2]
        self.deals.append(self.new_deal)
        self.dealCount += 1
        self.full = False
 
    def deal_count(self):
        return self.dealCount

    def reset_deal_count(self):
        self.dealCount = 0
        self.clear_deals()
 
    def update_title_name(self, x, name):
        self.deals[x][0] = name
 
    def title_name(self, dealIndex, start = None, end = None):
        return self.deals[dealIndex][0][start:end]
 
    def listing_side(self, x):
        return self.deals[x][1]
 
    def ms1(self, x):
        return self.deals[x][2]
 
    def buy_side(self, x):
        return self.deals[x][3]
 
    def ms2(self, x):
        return self.deals[x][4]
 
    def set_full(self, state):
        self.full = state
 
    def is_full(self): 
        return self.full
 
    @classmethod # Class Method
    def clear_deals(cls):
        cls.deals.clear()
