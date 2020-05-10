from typing import List, Set

from lib.article import Article
from lib.article_dict import ArticleDict


class SearchEngine:

    def __init__(self, collection: ArticleDict, search_string: str, title_search: bool = True, tag_search: bool = True,
                 description_search: bool = True):
        self._collection = collection
        self._title_search = title_search
        self._tag_search = tag_search
        self._description_search = description_search
        self._search_string = search_string

    def _search_title(self) -> List[Article]:
        result = list()
        for article in self._collection.values():
            if self._search_string in article.title:
                result.append(article)
        return result

    def search(self) -> ArticleDict:
        search_result = ArticleDict()
        if self._title_search:
            titles_found = self._search_title()
            for item in titles_found:
                search_result[item.uuid] = item
        return search_result
