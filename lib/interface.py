from collections import OrderedDict

from lib.article import Article
from lib.article_dict import ArticleDict


class ArticleInterface:

    def __init__(self):
        self._article_list = ArticleDict()

    def add_article(self, title: str, description: str = '', page: str = '', binder: str = '', tags: str = '') -> str:
        article = Article(title=title, description=description, page=page, binder=binder, tags=tags)
        self._article_list[article.uuid] = article
        return article.uuid

    @property
    def articles_list(self) -> OrderedDict:
        return self._article_list.sort_by_title()

    def get_article(self, uuid: str) -> Article:
        return self._article_list[uuid]

    def remove_article(self, uuid: str):
        del self._article_list[uuid]

    def edit_article(self, uuid: str, title: str = '', description: str = '', page: str = '', binder: str = '',
                     tags: str = ''):
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
