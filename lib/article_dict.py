import collections


class ArticleDict(dict):

    def __setitem__(self, key, value):
        if key in self.keys():
            raise AttributeError(f'Key "{key}" already exists')
        super().__setitem__(key, value)

    def sort_by_title(self) -> collections.OrderedDict:
        new_dict = collections.OrderedDict()
        new_list = list(self.values())
        new_list[:] = sorted(new_list, key=lambda list_item: list_item.title)
        for item in new_list:
            new_dict[item.uuid] = item
        return new_dict
