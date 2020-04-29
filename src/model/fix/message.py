from .field import Field
from .tag import Tag
from model.fix.enum.msg_type import MsgType
from model.fix.enum.ord_status import OrdStatus


class Message:
    _separator = '\x01'
    _fields = []
    _raw = None

    @property
    def fields(self):
        return self._fields

    @property
    def msg_type(self):
        field_content = None
        try:
            field_content = self.get_value(35)
            return MsgType(field_content) if field_content else None
        except ValueError:
            raise Exception('Invalid MsgType identified. {t}'.format(t=field_content))

    @property
    def ord_status(self):
        field_content = None
        if self.msg_type == MsgType.Execution_Report:
            try:
                field_content = self.get_value(39)
                return OrdStatus(field_content) if field_content else None
            except ValueError:
                raise Exception('Invalid OrdStatus identified. {s}'.format(s=field_content))
        else:
            return None

    @property
    def raw(self):
        return self._raw

    @staticmethod
    def _split_and_trim(text, sep):
        return [field.strip() for field in text.split(sep=sep)]

    def add_field(self, field: Field):
        self._fields.append(field)

    def parse(self, message: str):
        fields = self._split_and_trim(text=message, sep=self._separator)
        for field in fields:
            data = self._split_and_trim(text=field, sep='=')
            self._fields.append(Field(tag=data[0], content=data[1] if len(data) > 1 else None))

    def get_value(self, tag):
        try:
            if type(tag) == Tag:
                return next(field.content for field in self.fields if field.tag == tag)
            elif type(tag) == str and str(tag).isnumeric():
                return next(field.content for field in self.fields if field.tag.number == tag)
            elif type(tag) == int:
                return next(field.content for field in self.fields if field.tag.number == str(tag))
            else:
                return None
        except StopIteration:
            return None

    def __init__(self, message):
        self._fields.clear()
        self._raw = message
        self.parse(message)
