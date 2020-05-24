import unittest
import os
import json

from lib.article import Article
from lib.events import SAVE_NEEDED
from tests.test_data.article_test_data import ArticleTestData, ARTICLE_OPTIONAL_ATTRIBUTES

TEST_DATA_PATH = os.path.join(os.getcwd(), 'test_data', 'article.json')


class ModifyArticleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.initial_article_test_data = ArticleTestData(json_loaded['valid_article'])
        cls.modified_article_test_data = ArticleTestData(json_loaded['modified_article'])
        cls.invalid_article_test_data = ArticleTestData(json_loaded['invalid_article'])

    def tearDown(self) -> None:
        SAVE_NEEDED.clear()

    def _save_needed_test(self, msg):
        self.assertTrue(SAVE_NEEDED.is_set(), msg)
        SAVE_NEEDED.clear()

    def _attribute_setting_test(self, article, attribute, value):
        setattr(article, attribute, value)
        self.assertEqual(getattr(article, attribute), value, f'Verify {attribute} is set')
        self._save_needed_test(f'Verify save is needed after setting {attribute}')

    def _type_assertion_test(self, article, attribute, value):
        with self.assertRaises(TypeError,
                               msg=f'Verify exception is raised when modifying {attribute} with incorrect type of value'):
            setattr(article, attribute, value)
        self.assertFalse(SAVE_NEEDED.is_set(),
                         f'Verify save is not needed after exception of incorrect type for attribute {attribute}')

    def _prepare_article_with_title_only(self):
        article = Article(title=self.initial_article_test_data.title)
        SAVE_NEEDED.clear()
        return article

    def _prepare_article_with_all_fields(self):
        article = Article(title=self.initial_article_test_data.title,
                          description=self.initial_article_test_data.description,
                          page=self.initial_article_test_data.page, binder=self.initial_article_test_data.binder,
                          tags=self.initial_article_test_data.tags)
        SAVE_NEEDED.clear()
        return article

    def test_adding_attributes_values(self):
        article = self._prepare_article_with_title_only()
        for attribute in ARTICLE_OPTIONAL_ATTRIBUTES:
            self._attribute_setting_test(article, attribute, getattr(self.initial_article_test_data, attribute))

    def test_modifying_attributes_values(self):
        article = self._prepare_article_with_all_fields()
        self._attribute_setting_test(article, 'title', self.modified_article_test_data.title)
        for attribute in ARTICLE_OPTIONAL_ATTRIBUTES:
            self._attribute_setting_test(article, attribute, getattr(self.modified_article_test_data, attribute))

    def test_uuid_cannot_be_modified(self):
        article = self._prepare_article_with_title_only()
        with self.assertRaises(AttributeError, msg='Verify uuid cannot be modified'):
            article.uuid = 'modified uuid'
        self.assertFalse(SAVE_NEEDED.is_set(), 'Verify save is not needed after trying to modify uuid')

    def test_modifying_with_incorrect_type(self):
        article = self._prepare_article_with_all_fields()
        self._type_assertion_test(article, 'title', self.invalid_article_test_data.title)
        for attribute in ARTICLE_OPTIONAL_ATTRIBUTES:
            self._type_assertion_test(article, attribute, getattr(self.invalid_article_test_data, attribute))
