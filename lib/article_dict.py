import collections

from lib.events import SAVE_NEEDED
from lib.exceptions import DuplicatedArticle


class ArticleDict(dict):

    def __setitem__(self, key, value):
        if key in self.keys():
            raise DuplicatedArticle(f'Key "{key}" already exists')
        super().__setitem__(key, value)
        SAVE_NEEDED.set()

    def __delitem__(self, key):
        super().__delitem__(key)
        SAVE_NEEDED.set()

    def sort_by_title(self) -> collections.OrderedDict:
        new_dict = collections.OrderedDict()
        new_list = list(self.values())
        new_list[:] = sorted(new_list, key=lambda list_item: list_item.title)
        for item in new_list:
            new_dict[item.uuid] = item
        return new_dict
