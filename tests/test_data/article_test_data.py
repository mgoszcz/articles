from typing import List

ARTICLE_OPTIONAL_ATTRIBUTES = ['description', 'page', 'binder', 'tags']


class ArticleTestData:

    def __init__(self, article_dictionary: dict):
        self.title = article_dictionary['title']
        self.description = article_dictionary['description']
        self.page = article_dictionary['page']
        self.binder = article_dictionary['binder']
        self.tags = article_dictionary['tags']


class ArticleDictTestData:
    def __init__(self, articles_list: List[dict]):
        self.articles = [ArticleTestData(article) for article in articles_list]
