import pickle

import os


class SaveLoad:

    def __init__(self, articles_list, file_path='database.dat'):
        self.file_path = file_path
        self.articles_list = articles_list

    def save_data(self):
        data = {'articles_list': self.articles_list}
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'rb') as f:
            content = pickle.load(f)
        for key, value in content['articles_list'].items():
            self.articles_list[key] = value
