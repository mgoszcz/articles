import pandas

from lib.article import Article


class CSVImporter:

    def __init__(self, articles_list, file_path):
        self.articles_list = articles_list
        self.file_path = file_path

    def import_data(self):
        data = pandas.read_csv(self.file_path, sep=';')
        for i in data.index:
            article = Article(title=data['title'][i], description=data['description'][i], page=data['page'][i],
                              binder=data['page'][i], tags=data['tags'][i])
            self.articles_list[article.uuid] = article
