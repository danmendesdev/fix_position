from .block import Block


class BlockHeader:
    _fields = [8, 9, 35, 49, 56, 34]
    _block = None

    @property
    def block(self):
        return self._block

    def __init__(self):
        self._block = Block(name='Header', tags=self._fields)
