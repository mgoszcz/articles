import uuid
from typing import List

from lib.validators import Validators


class Article:

    @Validators.attribute_validator('title', str)
    @Validators.attribute_validator('description', str)
    @Validators.attribute_validator('page', str)
    @Validators.attribute_validator('binder', str)
    @Validators.attribute_validator('tags', list)
    def __init__(self, title: str, description: str = '', page: str = '', binder: str = '', tags: List[str] = None):
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
    @Validators.attribute_validator('value', str)
    def title(self, value: str):
        self._title = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @Validators.attribute_validator('value', str)
    def description(self, value: str):
        self._description = value

    @property
    def page(self) -> str:
        return self._page

    @page.setter
    @Validators.attribute_validator('value', str)
    def page(self, value: str):
        self._page = value

    @property
    def binder(self) -> str:
        return self._binder

    @binder.setter
    @Validators.attribute_validator('value', str)
    def binder(self, value: str):
        self._binder = value

    @property
    def tags(self) -> List[str]:
        if not self._tags:
            self._tags = list()
        return self._tags

    @tags.setter
    @Validators.attribute_validator('value', list)
    def tags(self, value: List[str]):
        self._tags = value

    @property
    def uuid(self) -> str:
        if not self._uuid:
            self.generate_uuid()
        return self._uuid

    def generate_uuid(self):
        self._uuid = uuid.uuid4().hex
