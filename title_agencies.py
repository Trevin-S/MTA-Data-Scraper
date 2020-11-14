class Title_Agencies:
 
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