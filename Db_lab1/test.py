from entity import country
from entity import city
from pickle import dump
from pickle import load
from dbms import dbms

db = dbms()

db.add_country("Ukraine", "Europe", "grn")
db.add_city("Kiev", 2000000, 12000, 0)
db.add_city("Lviv", 3000000, 55000, 0)
db.add_city("Cherkasy", 1500000, 54000, 0)
db.add_country("Poland", "Europe", "euro")
db.add_city("Varshava", 245000, 33000, 1)


#
# db.out_countries()
# db.out_cityes()
#
# db.del_city(1)
#
# print "==============="
# db.out_countries()
# db.out_cityes()

# def test(**kwargs):
#     for key, value in kwargs.iteritems():
#         print key + ': ' + value
#
# test(f1="foo", f2="bar")
