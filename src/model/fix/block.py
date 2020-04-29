from .field import Field


class Block:
    _name = None
    _fields = []

    @property
    def name(self):
        return self._name

    @property
    def fields(self):
        return self._fields

    def __init__(self, name, tags: []):
        self._name = name
        for tag in tags:
            self._fields.append(Field(tag=tag))
