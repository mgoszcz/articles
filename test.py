from lib.article import Article
from lib.article_dict import ArticleDict
from lib.interface import ArticleInterface

interface = ArticleInterface()
interface.import_csv('zagle.csv')
pass