class Agent:
 
    deals = [] # Class Attribute
 
    def __init__(self): # Instance Attributes
        self.dealCount = 0
        agent.clear_deals()
 
    def add_deal(self, titleName, listingSide, MS1, buySide, MS2): # Instance Methods / Procedural Attributes
        self.new_deal = [titleName, listingSide, MS1, buySide, MS2]
        self.deals.append(self.new_deal)
        self.deal_count += 1
        self.full = False
        self.paste_iteration = 0
 
    def deal_count(self):
        return self.deal_count
 
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

    def set_paste_iteration(self, number):
        self.paste_iteration = number

    def get_paste_iteration(self):
        return self.paste_iteration
 
    @classmethod # Class Method
    def clear_deals(cls):
        cls.deals.clear()