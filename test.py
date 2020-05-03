from lib.article import Article
from lib.article_dict import ArticleDict
from lib.interface import ArticleInterface

INTERFACE = ArticleInterface()

def print_articles():
    for article in INTERFACE.articles_list.values():
        print(article.title)
        print(f'\t{article.description}\n\t{article.binder}\n\t{article.page}')
        for tag in article.tags:
            print(f'\t\t{tag}')
        print(f'\t{article.uuid}')
        print('===============================================================')

print_articles()
pass