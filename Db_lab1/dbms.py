from entity import country
from entity import city

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
        self.countries[c_id].c_ids.append(c_id)
        self.cities[tmp.id] = tmp

    def del_city(self, id):
        if id in self.cities:
            self.countries[self.cities[id].c_id].c_ids.delete(id)
            del self.cities[id]
        else:
            print "There is no city with such id"

    def del_country(self, id):
        #TODO: make country deleteing
        return

    def find_city(self, value, field):
        #TODO: make searching by field
        return

    def task_fun(self):
        #TODO: resolve the task
        return



