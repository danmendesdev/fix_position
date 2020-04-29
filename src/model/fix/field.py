from .tag import Tag


class Field:
    _tag = None
    _content = None

    @property
    def tag(self):
        return self._tag

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def __init__(self, tag: int, content=None):
        self._tag = Tag(tag)
        self.content = content

    def __str__(self):
        return '{t}={c}'.format(t=self.tag.number, c=self.content)
