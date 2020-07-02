import os
import unittest
import json
from shutil import copy

from lib.article_collection import ArticleCollection
from lib.article_dict import ArticleDict
from lib.exceptions import InvalidUuidError
from tests.article.scripts import initializers, cleanups
from tests.article.scripts.environment import Environment
from tests.scripts import wait_methods
from tests.scripts.wait_methods import WaitMethods
from tests.test_data.article_test_data import ArticleDictTestData, ArticleTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')
WAIT_METHODS = WaitMethods()


class ArticleListTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.first_article = ArticleTestData(json_loaded['add_articles'][0])
        cls.second_article = ArticleTestData(json_loaded['add_articles'][1])

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()

    def setUp(self) -> None:
        self.article_collection = ArticleCollection()
        self.article_collection.add_new_article(self.first_article.title)
        self.remove_uuid = self.article_collection.add_new_article(self.second_article.title)
        WAIT_METHODS.wait_for_save_completed()

    def tearDown(self) -> None:
        del self.article_collection

    def test_removing_article(self):
        self.article_collection.remove_article(self.remove_uuid)
        self.assertEqual(len(self.article_collection.articles_list), 1, 'Verify len of articles list is 1 after remove')
        self.assertTrue(self.remove_uuid not in self.article_collection.articles_list.keys(),
                        'Verify article was removed')
        WAIT_METHODS.wait_for_save_completed()
        new_collection = ArticleCollection()
        self.assertEqual(len(new_collection.articles_list), 1, 'Verify len of articles list is 1 after load')
        self.assertTrue(self.remove_uuid not in new_collection.articles_list.keys(),
                        'Verify article is not present after load')

    def test_removing_article_invalid_uuid(self):
        with self.assertRaises(InvalidUuidError,
                               msg=f'Verify exception is raised when trying to remove article with invalid UUID'):
            self.article_collection.remove_article('0000000000000000000000000000000')