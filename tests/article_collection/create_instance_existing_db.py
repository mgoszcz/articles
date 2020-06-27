import os
import unittest
import json
from shutil import copy

from lib.article_collection import ArticleCollection
from tests.article.scripts import initializers, cleanups
from tests.article.scripts.environment import Environment
from tests.scripts.verifiers import Verifiers
from tests.test_data.article_test_data import ArticleDictTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class CreateInstanceNoDatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        copy(os.path.join(Environment().test_data_path, 'database_for_test.dat'), Environment().database_file)
        cls.article_collection = ArticleCollection()
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.articles_to_add = ArticleDictTestData(json_loaded['add_articles'])

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()
        cls.article_collection._auto_save.stop.set()

    def test_create_instance(self):
        self.assertIsInstance(self.article_collection, ArticleCollection,
                              'Verify created instance is ArticleCollection instance')
        self.assertTrue(self.article_collection._auto_save.is_alive(), 'Verify auto save is started')
        self.assertNotEqual(len(self.article_collection.articles_list), 0, 'Verify articles list is not empty')

    def test_verify_database_content(self):
        Verifiers().verify_articles_in_dictionary(self.article_collection.articles_list, self.articles_to_add)
