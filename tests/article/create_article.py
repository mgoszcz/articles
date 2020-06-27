import os
import json
import unittest

from lib.article import Article
from lib.events import SAVE_NEEDED
from tests.scripts.verifiers import Verifiers
from tests.test_data.article_test_data import ArticleTestData

TEST_DATA_PATH = os.path.join(os.getcwd(), 'test_data', 'article.json')


class CreateArticleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.valid_article_test_data = ArticleTestData(json_loaded['valid_article'])
        cls.invalid_article_test_data = ArticleTestData(json_loaded['invalid_article'])

    def tearDown(self) -> None:
        SAVE_NEEDED.clear()

    def _type_assertion_test(self, title, msg, description='', page='', binder='', tags=None):
        if not tags:
            tags = []
        with self.assertRaises(TypeError, msg=msg):
            Article(title=title, description=description, page=page, binder=binder, tags=tags)

    def test_create_article_no_title(self):
        with self.assertRaises(TypeError,
                               msg='Verify exception is raised when creating Article instance without title'):
            Article()
        self.assertFalse(SAVE_NEEDED.is_set())

    def test_create_article_with_title_only(self):
        article = Article(title=self.valid_article_test_data.title)
        self.assertIsInstance(article, Article, 'Verify added article is instance of Article class')
        Verifiers().verify_article_with_title_only(article=article, reference_article=self.valid_article_test_data)
        self.assertTrue(SAVE_NEEDED.is_set(), 'Verify save needed is set')

    def test_create_article_with_all_fields(self):
        article = Article(title=self.valid_article_test_data.title,
                          description=self.valid_article_test_data.description, page=self.valid_article_test_data.page,
                          binder=self.valid_article_test_data.binder, tags=self.valid_article_test_data.tags)
        self.assertIsInstance(article, Article, 'Verify added article is instance of Article class')
        Verifiers().verify_article_with_all_fields(article=article, reference_article=self.valid_article_test_data)
        self.assertTrue(SAVE_NEEDED.is_set(), 'Verify save needed is set')

    def test_create_article_invalid_types(self):
        self._type_assertion_test(self.invalid_article_test_data.title,
                                  msg='Verify exception is raised when title is incorrect type')
        self._type_assertion_test(self.valid_article_test_data.title,
                                  description=self.invalid_article_test_data.description,
                                  msg='Verify exception is raised when description is incorrect type')
        self._type_assertion_test(self.valid_article_test_data.title,
                                  page=self.invalid_article_test_data.page,
                                  msg='Verify exception is raised when page is incorrect type')
        self._type_assertion_test(self.valid_article_test_data.title,
                                  binder=self.invalid_article_test_data.binder,
                                  msg='Verify exception is raised when binder is incorrect type')
        self._type_assertion_test(self.valid_article_test_data.title,
                                  tags=self.invalid_article_test_data.tags,
                                  msg='Verify exception is raised when tags is incorrect type')
        self.assertFalse(SAVE_NEEDED.is_set())
