from .existing_tags import ExistingTags


class Tag:
    _number = 0
    _name = ''

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    def __init__(self, number: int):
        self._number = number
        try:
            self._name = ExistingTags(number).name
        except ValueError:
            self._name = 'Missing Tag Name'

    def __str__(self):
        return '{nu} ({na})'.format(nu=self.number, na=self.name)