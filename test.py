from lib.article import Article
from lib.article_dict import ArticleDict


lista = ArticleDict()
a = Article('mors')
b = Article('dupa')
c = Article('alfabet')
d = Article('zupa')
lista[a.uuid] = a
lista[b.uuid] = a
lista[b.uuid] = b
lista[c.uuid] = c
lista[d.uuid] = d
sorted_articles = lista.sort_by_title()

for item in sorted_articles.values():
    print(item.title)
