from entity import country
from entity import city
from pickle import dump
from pickle import load
from dbms import dbms

db = dbms()

db.add_country("Ukraine", "Europe", "grn")
db.add_city("Kiev", 150000, 12000, 0)

db.out_countries()
db.out_cityes()
