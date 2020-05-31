import unittest
import os
import json

from lib.article import Article
from lib.article_dict import ArticleDict
from lib.events import SAVE_NEEDED
from lib.exceptions import DuplicatedArticle
from tests.test_data.article_test_data import ArticleDictTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class ArticleDictTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.articles_to_add = ArticleDictTestData(json_loaded['add_articles'])
        cls.sorting_articles = json_loaded['sorting_test']

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
            self.assertEqual(article_dict[article.uuid], article, 'Verify article is added')
            self._save_needed_test('Verify save is needed after adding article')

    def test_sorting_articles(self):
        article_dict = ArticleDict()
        for article_title in self.sorting_articles:
            article = Article(title=article_title)
            article_dict[article.uuid] = article
        article_titles = [a.title for a in article_dict.sort_by_title().values()]
        self.sorting_articles.sort()
        self.assertEqual(article_titles, self.sorting_articles, 'Verify article dict is sorted')

    def test_add_article_with_the_same_uuid(self):
        article_dict = ArticleDict()
        article1 = Article(title='test1')
        article2 = Article(title='test2')
        article2._uuid = article1.uuid
        article_dict[article1.uuid] = article1
        SAVE_NEEDED.clear()
        with self.assertRaises(DuplicatedArticle,
                               msg=f'Verify exception is raised when adding article with the same uuid as existing'):
            article_dict[article2.uuid] = article2
        self.assertFalse(SAVE_NEEDED.is_set(),
                         f'Verify save is not needed after exception of duplicated uuid')
        self.assertEqual(len(article_dict), 1, 'Verify duplicated article was not added to ArticleDict')
