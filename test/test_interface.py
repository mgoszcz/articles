import json
import os
import unittest

from lib.interface import ArticleInterface

TEST_DATA_PATH = os.path.join(os.getcwd(), 'testdata', 'interface.json')


class InterfaceTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(TEST_DATA_PATH) as f:
            self.test_data = json.load(f)

    def test_adding_articles(self):
        added_articles = dict()
        interface = ArticleInterface()
        for article in self.test_data['add_articles']:
            uuid = interface.add_article(article['title'], article['description'], article['page'],
                                         article['binder'], article['tags'])
            added_articles[uuid] = article
        self.assertEqual(len(interface.articles_list), len(self.test_data['add_articles']),
                         'Verify articles count')
        for uuid, article in added_articles.items():
            article_in_interface = interface.get_article(uuid)
            for field_key, field_value in article.items():
                self.assertEqual(field_value, getattr(article_in_interface, field_key),
                                 f'Verify field {field_key} is corect')

    def test_sorting_articles(self):
        interface = ArticleInterface()
        for article in self.test_data['sorting_test']:
            interface.add_article(article)
        added_articles = [article.title for article in interface.articles_list.values()]
        self.assertEqual(sorted(self.test_data['sorting_test']), added_articles,
                         'Verify articles are sorted alphabetically')

    def test_removing_article(self):
        interface = ArticleInterface()
        uuids = list()
        for article in self.test_data['add_articles']:
            uuids.append(interface.add_article(article['title'], article['description'], article['page'],
                                               article['binder'], article['tags']))
        for uuid in uuids:
            interface.remove_article(uuid)
            self.assertFalse(uuid in interface.articles_list.keys(), 'Verify item was removed from articles list')
        self.assertEqual(len(interface.articles_list), 0, 'Verify articles list is empty')

    def test_modifying_article(self):
        interface = ArticleInterface()
        article = self.test_data['editing_test']
        title = article['title']
        description = article['description']
        page = article['page']
        binder = article['binder']
        tags = article['tags']
        uuid = interface.add_article(title, description, page, binder, tags)
        interface.edit_article(uuid=uuid, title=f'{title}_edited', description=f'{description}_edited',
                               page=f'{page}_edited', binder=f'{binder}_edited', tags=['tagi_edited'])
        self.assertEqual(interface.get_article(uuid).title, f'{title}_edited', 'Verify title was edited')
        self.assertEqual(interface.get_article(uuid).description, f'{description}_edited',
                         'Verify description was edited')
        self.assertEqual(interface.get_article(uuid).page, f'{page}_edited', 'Verify page was edited')
        self.assertEqual(interface.get_article(uuid).binder, f'{binder}_edited', 'Verify binder was edited')
        self.assertEqual(interface.get_article(uuid).tags, ['tagi_edited'], 'Verify tags was edited')
        interface.edit_article(uuid=uuid, title=f'{title}_edited2', binder=f'{binder}_edited2')
        self.assertEqual(interface.get_article(uuid).title, f'{title}_edited2', 'Verify title was edited')
        self.assertEqual(interface.get_article(uuid).description, f'{description}_edited',
                         'Verify description was edited')
        self.assertEqual(interface.get_article(uuid).page, f'{page}_edited', 'Verify page was edited')
        self.assertEqual(interface.get_article(uuid).binder, f'{binder}_edited2', 'Verify binder was edited')
        self.assertEqual(interface.get_article(uuid).tags, ['tagi_edited'], 'Verify tags was edited')
        interface.get_article(uuid).tags.append('tag_added')
        self.assertEqual(interface.get_article(uuid).tags, ['tagi_edited', 'tag_added'], 'Verify tag was added')
