import uuid


class Article:

    def __init__(self, title, description=None, page=None, binder=None, tags=None):
        self._title = title
        self._description = description
        self._page = page
        self._binder = binder
        self._tags = tags
        self._uuid = None

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def description(self) -> str:
        if not self._description:
            return ''
        else:
            return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def page(self) -> str:
        if not self._page:
            return ''
        else:
            return self._page

    @page.setter
    def page(self, value: str):
        self._page = value

    @property
    def binder(self) -> str:
        if not self._binder:
            return ''
        else:
            return self._binder

    @binder.setter
    def binder(self, value: str):
        self._binder = value

    @property
    def tags(self) -> str:
        if not self._tags:
            return ''
        else:
            return self._tags

    @tags.setter
    def tags(self, value: str):
        self._tags = value

    @property
    def uuid(self) -> str:
        if not self._uuid:
            self.generate_uuid()
        return self._uuid

    def generate_uuid(self):
        self._uuid = uuid.uuid4().hex
