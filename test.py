from lib.article import Article
from lib.article_dict import ArticleDict
from lib.article_collection import ArticleCollection
from lib.search_engine import SearchEngine
from lib.save_load import AutoSave

INTERFACE = ArticleCollection()

def print_articles(articles=INTERFACE.articles_list_sorted):
    for article in articles.values():
        print(article.title)
        # print(f'\t{article.description}\n\t{article.binder}\n\t{article.page}')
        # for tag in article.tags:
        #     print(f'\t\t{tag}')
        # print(f'\t{article.uuid}')
        print('===============================================================')

search = SearchEngine(INTERFACE.articles_list, 'wlochy')
search.search()
print_articles(search.search_results.sort_by_title())

print_articles()
pass