from collections import OrderedDict
from typing import List

from lib.article import Article
from lib.article_dict import ArticleDict
from lib.exceptions import DuplicatedArticle, InvalidUuidError
from lib.save_load import SaveLoad, AutoSave


class ArticleCollection:

    def __init__(self):
        self._article_list = ArticleDict()
        self.load_data()
        self._auto_save = AutoSave(self._article_list)
        self._auto_save.start()

    def __del__(self):
        self._auto_save.stop.set()

    def add_new_article(self, title: str, description: str = '', page: str = '', binder: str = '',
                        tags: List[str] = None) -> str:
        article = Article(title=title, description=description, page=page, binder=binder, tags=tags)
        try:
            self._article_list[article.uuid] = article
        except DuplicatedArticle:
            article.generate_uuid()
            self._article_list[article.uuid] = article
        return article.uuid

    def add_existing_article(self, article: Article):
        self._article_list[article.uuid] = article

    @property
    def articles_list(self) -> ArticleDict:
        return self._article_list

    @property
    def articles_list_sorted(self) -> OrderedDict:
        return self._article_list.sort_by_title()

    def get_article(self, uuid: str) -> Article:
        if uuid not in self._article_list.keys():
            raise InvalidUuidError(f'UUID: "{uuid}" does not exist')
        return self._article_list[uuid]

    def remove_article(self, uuid: str):
        if uuid not in self._article_list.keys():
            raise InvalidUuidError(f'UUID: "{uuid}" does not exist')
        del self._article_list[uuid]

    def edit_article(self, uuid: str, title: str = '', description: str = '', page: str = '', binder: str = '',
                     tags: List[str] = None):
        if uuid not in self._article_list.keys():
            raise InvalidUuidError(f'UUID: "{uuid}" does not exist')
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

    def load_data(self):
        save_load = SaveLoad(self._article_list)
        save_load.load_data()
