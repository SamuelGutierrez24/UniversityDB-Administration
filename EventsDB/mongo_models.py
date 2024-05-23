from mongoengine import Document, fields

class Event(Document):
    name = fields.StringField(required=True)
    description = fields.StringField()
    date = fields.DateTimeField()
    meta = {'collection': 'events'}
