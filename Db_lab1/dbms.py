from entity import country
from entity import city
from file_helper import file_helper

class dbms:
    id = 1
    name = 2
    mainl = 3
    currency = 4
    population = 5
    area = 6

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
        self.countries[c_id].c_ids.append(tmp.id)
        self.cities[tmp.id] = tmp

    def del_city(self, id):
        if id in self.cities:
            self.countries[self.cities[id].c_id].c_ids.remove(id)
            del self.cities[id]
        else:
            print "There is no city with such id"

    def del_country(self, id):
        if id in self.countries:
            for i in self.countries[id].c_ids:
                self.del_city(i)
            del self.countries[id]
        else:
            print "there is no country with such id"

    def find_city(self, value, field):
        #TODO: make searching by field
        return

    def collect_countries(self, filter):
        res = []
        for i in self.countries:
            if filter(self.countries[i]):
                res.append(self.countries[i])
        return res



