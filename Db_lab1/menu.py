from dbms import dbms

class menu:

    @staticmethod
    def main_menu():
        print "1 - Out database."
        print "2 - Add"
        print "3 - Update"
        print "4 - Delete"
        print "5 - Find"
        print "6 - exit"

    @staticmethod
    def select_menu():
        print "1 - country"
        print "2 - city"

    @staticmethod
    def start_menu(db):
        while True:
            menu.main_menu()
            key = input()
            if key == 1:
                db.out_countries()
            elif key == 2:
                menu.select_menu()
                key1 = input()
                if key1 == 1:
                    print "name (string):"
                    name = input()
                    print "mainland (string):"
                    mainl = input()
                    print "currency (int):"
                    curr = input()
                    db.add_country(name, mainl, curr)
                elif key1 == 2:
                    print "name (string):"
                    name = input()
                    print "population (int):"
                    population = input()
                    print "area (int):"
                    area = input()
                    db.add_country(name, population, area)
                else:
                    print "Wrong key!"
            elif key == 3:
                menu.select_menu()
                key1 = input()
                if key1 == 1:
                    print "id (int):"
                    id = input()
                    print "attribute (string):"
                    attr = input()
                    print "value:"
                    val = input()
                    db.update_country(id, attr, val)
                elif key1 == 2:
                    print "id (int):"
                    id = input()
                    print "attribute (string):"
                    attr = input()
                    print "value:"
                    val = input()
                    db.update_city(id, attr, val)
                else:
                    print "Wrong key!"
            elif key == 4:
                menu.select_menu()
                key1 = input()
                if key1 == 1:
                    print "id (int):"
                    id = input()
                    db.del_country(id)
                elif key1 == 2:
                    print "id (int):"
                    id = input()
                    db.delete_city(id)
                else:
                    print "Wrong key!"
            elif key == 5:
                dbms.out_lands(db.collect_countries(lambda x: db.task_filter(x)))
            elif key == 6:
                break
            else:
                print "Wrong key!"