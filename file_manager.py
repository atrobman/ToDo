from item import *
import pickle

class FileManager:

    @staticmethod
    def save_data(group, filepath="data.pkl"):

        if type(group) is not Group:
            raise TypeError(f"{repr(group)} not a Group (Type={type(group)})")
        
        with open(filepath, "wb") as file:
            pickle.dump(group, file, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_data(filepath="data.pkl"):

        load_group = None

        with open(filepath, "rb") as file:
            load_group = pickle.load(file)
        
        if type(load_group) is not Group:
            raise FileNotFoundError(f"Object at {filepath} not a group (Type={type(load_group)})")
        
        return load_group
            