"""
School Maker!

The idea here, is that students learn how to use dictionaries in Python by looking through a
'simplified' representation of a school in which there are hidden 'pigeons'. Once they've found
the pigeons, they've won.


"""

# We need to use UserX to create dict-like objects that we then
# modify to make things a little more difficult for the students.
from collections import UserDict, UserList, OrderedDict

# To create some degree of variation, we use random functions
# so that the same 'school' isn't created every time.
from random import random, randint, choice

# In order to transport the school to students computers without
# them being able to open it in a text editor, we pickle it instead.
import pickle

# We use fake to generate the random names, etc.
import faker

# Just to add that little bit of realism, we add some fake school data
# to the top level in the school dict.
from faker_education import SchoolProvider


# This will count how many pigeons we find when using our search
# function, essentially making sure there are pigeons in the data.
PIGEON_COUNT = 0

# Here we initialise the faker class. I want there to me 3 spanish
# results for every 1 english result.
FAKE = faker.Faker(
    OrderedDict([
        ("es_ES", 3),
        ("en_GB", 1)
        ]
    )
)


school_fake = faker.Faker()
school_fake.add_provider(SchoolProvider)


class Pigeon:
    """
    Pigeon

    Simple representation of a pigeon.

    """
    def __init__(self):
        self.caught = False
        self.name = FAKE.first_name()

    def __repr__(self):
        return "Pigeon!"

    def catch(self):
        if not self.caught:
            self.caught = True if random() > 0.5 else False


def create_pigeon():
    return Pigeon()


def search_pigeons(data, path=[]):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = path + [key]
            if isinstance(value, Pigeon):
                print(f'Found Pigeon at path: {new_path}')
            else:
                search_pigeons(value, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = path + [i]
            print(new_path)
            search_pigeons(item, new_path)



def add_pigeons():
    pigeons = [create_pigeon() for i in range(5)]

    while pigeons:
        if random() > 0.97:
            global PIGEON_COUNT
            PIGEON_COUNT += 1
            yield pigeons.pop()
        else:
            yield {}
    else:
        while True:
            yield {}


def str_only_repr(v):
    if isinstance(v, (str, int, bool)):
        return repr(v)
    else:
        return "..."


class MyDict(UserDict):

    def __init__(self, data):
        global PIGEON_COUNT

        if random() > 0.9995:
            data['pigeon'] = create_pigeon()
            print("Pigeon Added")
            PIGEON_COUNT += 1
        UserDict.__init__(self, data)

    def __repr__(self):
        # return repr(set(self.data.keys()))
        return repr({k: str_only_repr(v) for k, v in self.data.items()})

class MyList(UserList):
    def __repr__(self):
        return repr([x for x in range(len(self.data))])


def create_table():
    return MyDict({
        "OnIt":{},
        "UnderIt":{}
    })


def create_chair(desk_number, student):
    return MyDict({
        "number": desk_number,
        "person": student,
        "UnderIt": {} if randint(0,1) else {"bag": {}}
    })


def create_tv():
    return MyDict({
        "Make": "LG",
        "Model": "An Average One",
        "OnOrOff": randint(0,1)
    })


def create_book():
    return MyDict({
        "isbn": FAKE.isbn10(),
    })


def create_shelf(x):
    return MyDict({
        "books": [
            create_book() for x in range(randint(1,5))
        ],
        "shelf_number": x,
        "creaky": False if random() > 0.4 else True
    })


def create_bookcase():
    return MyDict({
        "shelves": [
            create_shelf(x) for x in range(randint(2,4))
        ]
    })


def create_pc():
    return MyDict({
        "make": choice(["HP", "DELL", "Apple", "ACER", "ASUS"]),
        "model": choice(["cheap", "middle", "expensive"]),
        "HDD Status": "Full" if random() > 0.9 else "Not Full",
        "on": True if random() > 0.5 else False
    })


def create_student(age):
    return MyDict({
        "name": FAKE.name(),
        "age": age,
        "paying_attention": True if random() > 0.3 else False,
        "scared_of_pigeons": True if random() > 0.97 else False
    })


def create_teacher():
    return MyDict({
        "name": FAKE.name(),
        "age": "Never you mind...",
        "scared_of_pigeons": True if random() > 0.70 else False
    })


def create_unique_room():
    return MyDict({})


def create_room():
    return MyDict({

    })


def create_department():
    return MyDict({
        "name": choice(["English", "Maths", "Science", "History", "RE", "DT", "MFL", "ALC"])
    })


def create_floor():
    return MyDict({})


def create_building(buildings):
    return MyDict({
        'name': choice(buildings),
        'floors': [create_floor() for x in range(randint(2,4))]
    })

def create_school():
    s = MyDict({})

    s['name'] = ""
    s['address'] = FAKE.address()
    s['buildings'] = []

    return s


def create_westside():

    s = MyDict({})

    for k, v in school_fake.school_object().items():
        s[k] = v

    buildings = ["East Wing", "Main Building", "The Quad", "Block A"]

    s['buildings'] = [create_building(buildings), create_building(buildings)]

    for building in s['buildings']:

        for floor in building['floors']:
            floor['departments'] = [create_department() for x in range(randint(3,8))]
            floor['number_of_rooms'] = 0
            floor['number_of_departments'] = len(floor['departments'])

            for department in floor['departments']:
                department['rooms'] = [create_room() for x in range(randint(1, 5))]

                floor['number_of_rooms'] += len(department['rooms'])



                for room in department['rooms']:
                    age = randint(11,16)
                    room['people'] = {
                        "teacher": create_teacher(),
                        "students": [create_student(age) for x in range(randint(20, 32))]
                    }
                    num_desks = randint(25, 30)
                    num_students = len(room['people']['students'])
                    room['equipment'] = {
                        "tv": [create_tv() for x in range(randint(1,2))],
                        "pcs": [create_pc() for x in range(num_desks)],
                        "furniture": {
                            "chairs": [create_chair(x, room['people']['students'][min(x,
                                                                                      num_students-1)]) for x in range(num_desks)],
                            "tables": [create_table() for x in range(num_desks)],
                            "bookcases": [create_bookcase() for x in range(randint(1,5))]
                        }
                    }

    return s


if __name__ == "__main__":
    x = create_westside()

    search_pigeons(x)

    print(PIGEON_COUNT)


    with open("school.pickle", "wb") as f:
        pickle.dump(x, f)

    with open("pigeons.txt", "w") as f:
        f.write(str(x))



