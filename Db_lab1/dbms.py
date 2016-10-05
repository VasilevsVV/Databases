from entity import country
from entity import city

class dbms:

    def __init__(self):
        self.countries = {}
        self.cities = {}

    def out_countries(self):
        for i in self.countries:
            self.countries[i].out()

    def out_cityes(self):
        for i in self.cities:
           self.cities[i].out()

    def add_country(self,name, mainl, curr):
        tmp = country(name, mainl, curr)
        self.countries[tmp.id] = tmp

    def add_city(self, name, popul, area, c_id):
        tmp = city(name, popul, area, c_id)
        if c_id not in self.countries:
            print "There are no such country."
            return
        self.countries[c_id].c_ids.append(c_id)
        self.cities[tmp.id] = tmp



