import unittest

from lib.article_collection import ArticleCollection
from tests.article.scripts import initializers, cleanups


class CreateInstanceNoDatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        cls.article_collection = ArticleCollection()

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()
        cls.article_collection._auto_save.stop.set()

    def test_create_instance_no_database(self):
        self.assertIsInstance(self.article_collection, ArticleCollection,
                              'Verify created instance is ArticleCollection instance')
        self.assertTrue(self.article_collection._auto_save.is_alive(), 'Verify auto save is started')
        self.assertEqual(len(self.article_collection.articles_list), 0, 'Verify articles list is empty')

