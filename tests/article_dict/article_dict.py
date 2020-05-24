import unittest
import os
import json

from lib.article import Article
from lib.article_dict import ArticleDict
from lib.events import SAVE_NEEDED
from tests.test_data.article_test_data import ArticleDictTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class ArticleDictTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.articles_to_add = ArticleDictTestData(json_loaded['add_articles'])

    def tearDown(self) -> None:
        SAVE_NEEDED.clear()

    def _save_needed_test(self, msg):
        self.assertTrue(SAVE_NEEDED.is_set(), msg)
        SAVE_NEEDED.clear()

    def test_create_article_dict(self):
        article_dict = ArticleDict()
        self.assertIsInstance(article_dict, ArticleDict, 'Verify created instance is type of ArticleDict')

    def test_adding_articles(self):
        article_dict = ArticleDict()
        for article_data in self.articles_to_add.articles:
            article = Article(title=article_data.title, description=article_data.description, page=article_data.page,
                              binder=article_data.binder, tags=article_data.tags)
            article_dict[article.uuid] = article
            self.assertEqual(article_dict[article.uuid], article, 'Verfy article is added')
            self._save_needed_test('Verify save is needed after adding article')

