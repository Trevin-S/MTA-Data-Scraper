# Classes
 
# Attributes - Variable which holds value inside a class. Two types:
# Instance Attributes - Unique for seperate instances *SELF.VARIABLE*
# Class Attributes - Shared among all instances of class, also usable without instance, accesible via class name *STANDARD VARIABLE OUTSIDE METHODS*
 
# Methods - Fucntions inside classes
# Instance Methods / Procedural Attributes - Unique per instance, interacts with instance attributes. *SELF IS ALWAYS FIRST PARAM*
# Class Methods - Shared among all instances, accesible with no instance via class name. Interacts with class attributes *CLS IS ALWAYS FIRST PARAM*
 
# Getters - Method which "Gets" or returns some attribute 
# Setters - Method which "Sets" or assigns some value to some attribute
 
# Special Methods (dunder methods)
# __init__  instance constructor - creates new instance of the object
# __del__()  instance destructor - destroys object when no longer needed. Rarely used, python mem management handles destruction automatically.
 
class user():
 
    def __init__(self):
        # User credentials
        # 'gracie'
        # 'Wallace1'
        # 'serraa'
        # 'Dreamteam'
        self.usernames = ['trevins','gracie','serraa']
        self.password = read(open("password.txt", "r"))
        self.paused = False
        self.lastState = False
        self.running = True
 
    def select_user(self, userIndex):
        self.username = self.usernames[userIndex]
 
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
 
    def add_long_agency(self, agency):
        self.titleAgenciesShort.append(agency)
 
    def add_short_agency(self, agency):
        self.titleAgenciesShort.append(agency)
 
    def agency_count(self):
        return len(self.titleAgenciesLong)
 
    def short_agency(self, index, start = None, end = None):
        return self.titleAgenciesShort[index][start:end]
 
    def long_agency(self, index, start = None, end = None):
        return self.titleAgenciesLong[index][start:end]
 
class agent:
 
    deals = [] # Class Attribute
 
    def __init__(self): # Instance Attributes
        self.dealCount = 0
        agent.clear_deals()
 
    def add_deal(self, titleName, listingSide, MS1, buySide, MS2): # Instance Methods / Procedural Attributes
        self.new_deal = [titleName, listingSide, MS1, buySide, MS2]
        self.deals.append(self.new_deal)
        self.dealCount += 1
        self.full = False
 
    def deal_count(self):
        return self.dealCount
 
    def update_title_name(self, x, name):
        self.deals[x][1] = name
 
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