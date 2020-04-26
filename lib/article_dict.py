import collections


class ArticleDict(dict):

    def sort_by_title(self) -> collections.OrderedDict:
        new_dict = collections.OrderedDict()
        new_list = list(self.values())
        new_list[:] = sorted(new_list, key=lambda item: item.title)
        for item in new_list:
            new_dict[item.uuid] = item
        return new_dict
