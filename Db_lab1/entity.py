class country:

    def __init__(self, id , name, mainl, currency):
        self.id = id
        self.name = name
        self.mainl = mainl
        self.currency = currency

    # def make_string(self):
    #     return self.name + ':' + self.mainl + ':' + str(self.currency)


class city:

    def __init__(self, id, name, population, area):
        self.id = id
        self.name = name
        self.population = population
        self.area = area
