from typing import List

from lib.article import Article
from lib.article_dict import ArticleDict
from lib.exceptions import DuplicatedArticle


class SearchEngine:

    #TODO: ignoruj polskie znaki i w chuj testów

    def __init__(self, collection: ArticleDict, search_string: str, title_search: bool = True, tag_search: bool = True,
                 description_search: bool = True):
        self._collection = collection
        self._title_search = title_search
        self._tag_search = tag_search
        self._description_search = description_search
        self._search_string = search_string
        self._search_results = ArticleDict()

    def _search_title(self) -> List[Article]:
        result = list()
        for article in self._collection.values():
            if self._search_string.lower() in article.title.lower():
                result.append(article)
        return result

    def _search_tag(self) -> List[Article]:
        result = list()
        for article in self._collection.values():
            for tag in article.tags:
                if self._search_string.lower() in tag.lower():
                    result.append(article)
                    break
        return result

    def _search_description(self) -> List[Article]:
        result = list()
        for article in self._collection.values():
            if self._search_string.lower() in article.description.lower():
                result.append(article)
        return result

    def _add_found_items(self, found_items):
        for item in found_items:
            try:
                self._search_results[item.uuid] = item
            except DuplicatedArticle:
                pass

    @property
    def search_results(self) -> ArticleDict:
        return self._search_results

    def search(self):
        if self._title_search:
            items_found = self._search_title()
            self._add_found_items(items_found)
        if self._tag_search:
            items_found = self._search_tag()
            self._add_found_items(items_found)
        if self._description_search:
            items_found = self._search_description()
            self._add_found_items(items_found)
