from lib.article import Article
from lib.article_dict import ArticleDict
from lib.interface import ArticleInterface
from lib.search_engine import SearchEngine

INTERFACE = ArticleInterface()

def print_articles(articles=INTERFACE.articles_list_sorted):
    for article in articles.values():
        print(article.title)
        # print(f'\t{article.description}\n\t{article.binder}\n\t{article.page}')
        # for tag in article.tags:
        #     print(f'\t\t{tag}')
        # print(f'\t{article.uuid}')
        print('===============================================================')

search = SearchEngine(INTERFACE.articles_list, 'Chorwacja')
search.search()

print_articles()
pass