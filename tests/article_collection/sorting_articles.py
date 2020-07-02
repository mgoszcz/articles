import os
import unittest
import json

from lib.article_collection import ArticleCollection
from tests.article.scripts import initializers, cleanups
from tests.test_data.article_test_data import ArticleDictTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class SortingArticlesTest(unittest.TestCase):
    article_collection = None

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        cls.article_collection = ArticleCollection()
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.sorting_articles = ArticleDictTestData(json_loaded['sorting_articles'])

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()
        del cls.article_collection

    def test_sorting_articles(self):
        reference_articles_list = self.sorting_articles.articles
        for article in reference_articles_list:
            self.article_collection.add_new_article(title=article.title,
                                                    description=article.description,
                                                    page=article.page,
                                                    binder=article.binder,
                                                    tags=article.tags)
        sorted_articles_titles = [article.title for article in self.article_collection.articles_list_sorted.values()]
        articles_titles_reference = [article.title for article in reference_articles_list]
        self.assertEqual(sorted_articles_titles, sorted(articles_titles_reference),
                         'Verify sorted articles returned from articles collection are properly sorted')
