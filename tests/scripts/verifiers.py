import unittest

from lib.article import Article
from lib.article_dict import ArticleDict
from tests.test_data.article_test_data import ArticleDictTestData, ArticleTestData


class Verifiers(unittest.TestCase):

    def verify_articles_in_dictionary(self, dictionary: ArticleDict, test_data: ArticleDictTestData):
        self.assertEqual(len(dictionary), len(test_data.articles), 'Verify count of articles is correct')
        for test_data_article in test_data.articles:
            passed = False
            for article in dictionary.values():
                if test_data_article.title == article.title:
                    if test_data_article.page != article.page:
                        continue
                    if test_data_article.description != article.description:
                        continue
                    if test_data_article.binder != article.binder:
                        continue
                    if test_data_article.tags != article.tags:
                        continue
                    passed = True
            self.assertTrue(passed,
                            f'Verify article is present: title: {test_data_article.title}, '
                            f'\n\tdescription: {test_data_article.description}, \n\tpage: {test_data_article.page}, '
                            f'\n\tbinder: {test_data_article.binder}, \n\ttags: {test_data_article.tags}')

    def verify_article_with_title_only(self, article: Article, reference_article: ArticleTestData):
        self.assertEqual(article.title, reference_article.title, 'Verify proper title is created')
        self.assertEqual(article.description, '', 'Verify description is empty string')
        self.assertEqual(article.binder, '', 'Verify binder is empty string')
        self.assertEqual(article.page, '', 'Verify page is empty string')
        self.assertEqual(article.tags, [], 'Verify tags is empty list')
        self.assertNotEqual(article.uuid, None, 'Verify uuid is created')

    def verify_article_with_all_fields(self, article: Article, reference_article: ArticleTestData):
        self.assertEqual(article.title, reference_article.title, 'Verify proper title is created')
        self.assertEqual(article.description, reference_article.description,
                         'Verify proper description is created')
        self.assertEqual(article.binder, reference_article.binder, 'Verify proper binder is created')
        self.assertEqual(article.page, reference_article.page, 'Verify proper page is created')
        self.assertEqual(article.tags, reference_article.tags, 'Verify proper tags are created')
        self.assertNotEqual(article.uuid, None, 'Verify uuid is created')