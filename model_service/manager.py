import os
import pathlib

class Manager(object):
    def __init__(self) -> None:
        self.storage_path = '/data/models'

    def get_model_save_path(self, name):
        return os.path.join(self.storage_path, name)

    def get_model_weight_path(self, name):
        return os.path.join(self.get_model_save_path(name), 'weight')

    def get_model_code_path(self, name):
        return os.path.join(self.get_model_save_path(name), 'code')

    def get_model_result_path(self, name):
        return os.path.join(self.get_model_save_path(name), 'result')

