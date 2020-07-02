import os
import unittest
import json
from shutil import copy

from lib.article_collection import ArticleCollection
from lib.article_dict import ArticleDict
from lib.exceptions import InvalidUuidError
from tests.article.scripts import initializers, cleanups
from tests.article.scripts.environment import Environment
from tests.test_data.article_test_data import ArticleDictTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class ArticleListTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        copy(os.path.join(Environment().test_data_path, 'database_for_test.dat'), Environment().database_file)
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.articles_to_add = ArticleDictTestData(json_loaded['add_articles'])
        cls.sorting_articles = json_loaded['sorting_test']

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()

    def setUp(self) -> None:
        self.article_collection = ArticleCollection()

    def tearDown(self) -> None:
        del self.article_collection

    def test_attribute_articles_list(self):
        self.assertIsInstance(self.article_collection._article_list, ArticleDict,
                              'Verify _articles_list is ArticleDict instance')

    def test_get_article(self):
        for article in self.article_collection.articles_list.values():
            self.assertEqual(article, self.article_collection.get_article(article.uuid),
                             'Verify article returned by get_article is correct')

    def test_get_article_incorrect_uuid(self):
        with self.assertRaises(InvalidUuidError,
                               msg=f'Verify exception is raised when trying to get article with invalid UUID'):
            self.article_collection.get_article('0000000000000000000000000000000')
