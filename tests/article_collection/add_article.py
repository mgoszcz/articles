import unittest
import json
import os

from lib.article import Article
from lib.article_collection import ArticleCollection
from tests.article.scripts import initializers, cleanups
from tests.scripts.verifiers import Verifiers
from tests.scripts.wait_methods import WaitMethods
from tests.test_data.article_test_data import ArticleTestData

TEST_DATA_PATH = os.path.join('..', 'test_data', 'articles_simple.json')


class AddArticleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        initializers.initialize_save_test()
        with open(TEST_DATA_PATH) as f:
            json_loaded = json.load(f)
        cls.first_article = ArticleTestData(json_loaded['add_articles'][0])
        cls.second_article = ArticleTestData(json_loaded['add_articles'][1])

    def setUp(self) -> None:
        self.article_collection = ArticleCollection()

    def tearDown(self) -> None:
        del self.article_collection

    @classmethod
    def tearDownClass(cls) -> None:
        cleanups.cleanup_save_test()

    def test_add_article_with_title_only(self):
        article_uuid = self.article_collection.add_new_article(title=self.first_article.title)
        article = self.article_collection.get_article(article_uuid)
        Verifiers().verify_article_with_title_only(article=article, reference_article=self.first_article)
        WaitMethods().wait_for_save_completed()
        new_collection = ArticleCollection()
        self.assertTrue(article_uuid in new_collection.articles_list.keys(),
                        'Verify new article uuid is present when creating new article collection (loaded from saved file)')
        Verifiers().verify_article_with_title_only(article=new_collection.get_article(article_uuid),
                                                   reference_article=self.first_article)

    def test_add_article_with_all_fields(self):
        article_uuid = self.article_collection.add_new_article(title=self.second_article.title,
                                                               description=self.second_article.description,
                                                               page=self.second_article.page,
                                                               binder=self.second_article.binder,
                                                               tags=self.second_article.tags)
        article = self.article_collection.get_article(article_uuid)
        Verifiers().verify_article_with_all_fields(article=article, reference_article=self.second_article)
        WaitMethods().wait_for_save_completed()
        new_collection = ArticleCollection()
        self.assertTrue(article_uuid in new_collection.articles_list.keys(),
                        'Verify new article uuid is present when creating new article collection (loaded from saved file)')
        Verifiers().verify_article_with_all_fields(article=new_collection.get_article(article_uuid),
                                                   reference_article=self.second_article)

    def test_add_existing_article(self):
        article = Article(title=self.second_article.title, description=self.second_article.description,
                          page=self.second_article.page,
                          binder=self.second_article.binder,
                          tags=self.second_article.tags)
        self.article_collection.add_existing_article(article)
        Verifiers().verify_article_with_all_fields(article=self.article_collection.get_article(article.uuid),
                                                   reference_article=self.second_article)
        WaitMethods().wait_for_save_completed()
        new_collection = ArticleCollection()
        self.assertTrue(article.uuid in new_collection.articles_list.keys(),
                        'Verify new article uuid is present when creating new article collection (loaded from saved file)')
        Verifiers().verify_article_with_all_fields(article=new_collection.get_article(article.uuid),
                                                   reference_article=self.second_article)
