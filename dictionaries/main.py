
import pickle

from school_maker import Pigeon, MyDict, MyList


with open("school.pickle", "rb") as school_file:
    school_dict = pickle.load(school_file)


print(school_dict)

