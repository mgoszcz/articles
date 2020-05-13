from __future__ import annotations
import pickle

import os
from threading import Thread, Event
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.article_dict import ArticleDict


class AutoSave(Thread):
    __save_needed = Event()
    __auto_save_paused = Event()

    def __init__(self, collection: ArticleDict):
        super(AutoSave, self).__init__()
        self._collection = collection
        self.stop = Event()

    # def _verify_collection_content_changed(self, collection_snapshot):
    #     for key, value in collection_snapshot

    def run(self):
        while not self.stop.is_set():
            if AutoSave.__save_needed.is_set():
                print('Save needed, save data')
                SaveLoad(self._collection).save_data()
                AutoSave.__save_needed.clear()
            time.sleep(5)

    @classmethod
    def trigger_save(cls):
        if not cls.__auto_save_paused.is_set():
            cls.__save_needed.set()
        else:
            print('Auto Save is paused now')

    @classmethod
    def pause_auto_save(cls):
        cls.__auto_save_paused.set()

    @classmethod
    def unpause_auto_save(cls):
        cls.__auto_save_paused.clear()


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
        AutoSave.pause_auto_save()
        with open(self.file_path, 'rb') as f:
            content = pickle.load(f)
        for key, value in content['articles_list'].items():
            self.articles_list[key] = value
        AutoSave.unpause_auto_save()
