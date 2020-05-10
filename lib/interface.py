from collections import OrderedDict
from typing import List

from lib.article import Article
from lib.article_dict import ArticleDict
from lib.csv_importer import CSVImporter
from lib.save_load import SaveLoad


class ArticleInterface:

    def __init__(self):
        self._article_list = ArticleDict()
        self.load_data()

    def add_article(self, title: str, description: str = '', page: str = '', binder: str = '',
                    tags: List[str] = None) -> str:
        article = Article(title=title, description=description, page=page, binder=binder, tags=tags)
        try:
            self._article_list[article.uuid] = article
        except AttributeError:
            article.generate_uuid()
            self._article_list[article.uuid] = article
        self.save_data()
        return article.uuid

    @property
    def articles_list(self) -> ArticleDict:
        return self._article_list

    @property
    def articles_list_sorted(self) -> OrderedDict:
        return self._article_list.sort_by_title()

    def get_article(self, uuid: str) -> Article:
        return self._article_list[uuid]

    def remove_article(self, uuid: str):
        del self._article_list[uuid]
        self.save_data()

    def edit_article(self, uuid: str, title: str = '', description: str = '', page: str = '', binder: str = '',
                     tags: List[str] = None):
        article = self.get_article(uuid)
        if title:
            article.title = title
        if description:
            article.description = description
        if page:
            article.page = page
        if binder:
            article.binder = binder
        if tags:
            article.tags = tags
        self.save_data()

    def import_csv(self, file_path):
        csv_importer = CSVImporter(self._article_list, file_path)
        csv_importer.import_data()
        self.save_data()

    def load_data(self):
        save_load = SaveLoad(self._article_list)
        save_load.load_data()

    def save_data(self):
        save_load = SaveLoad(self._article_list)
        save_load.save_data()
